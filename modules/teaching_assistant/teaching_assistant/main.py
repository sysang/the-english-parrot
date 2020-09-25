import json
import re
import random
from os.path import dirname

from yaml import load
from yaml import CLoader as Loader
from jinja2 import Template

from teaching_assistant.devutils import showlist


class Lesson(object):
    def __init__(self, datapath):
        self._data = self.ingest_data(datapath)
        self.topic = self._data['topic']
        self.dialogue_turns = self._data['dialogueTurns']
        self.dialogue_length = len(self.dialogue_turns)

    def ingest_data(self, datapath):
        document = open(datapath)
        parsed = load(document, Loader=Loader)

        return parsed['story']

    def get_turn_data(self, progress):
        for turn in self.dialogue_turns:
            if turn['progress'] == progress:
                print(turn)
                return turn

        raise ValueError("Invalid progress value")

    def create_turn(self, data):
        return DialogueTurn(
                    topic=self.topic,
                    question=data['question'],
                    scenario_case=data['scenarios']['main']['name'],
                    scenario=data['scenarios']['main'],
                    progress=data['progress'],
                    going_next=data['going_next'],
                    is_last=data['progress'] == (self.dialogue_length - 1)
                )

    def compile(self):
        content = ''
        for data in self.dialogue_turns:
            turn = self.create_turn(data)
            content += turn.compile() + '\n' + turn.compile_next_checkpoint() + '\n'

        return content


class DialogueTurn(object):
    def __init__(self, topic, question, scenario_case, scenario, progress, going_next, is_last):
        self.nlu_confused = None
        self.nlu_confident = self.define_status(True)  # 'positive' or None because any value except None will be treated as 1 (True)
        self.will_return = None

        self._question = question
        self._going_next = going_next
        self._topic = topic
        self.is_last = is_last
        self.scenario_case = scenario_case
        self.scenario = scenario
        self.progress = progress
        self.intention = self.scenario['intention']
        self.utterances = self.scenario['utterances']
        self.entities = self.parse_entities()

        self.question = self.makeup_question_signature(self._question)
        self.going_next = self.makeup_question_signature(self._going_next)
        self.topic = self.transform_to_snake_case(topic)
        self.json_entities = json.dumps(self.entities)
        self.json_slots = self.get_action_storing_lesson_slots()

    def define_status(self, status=None):
        if status:
            return 'positive'

        return None

    def json_stringify_entities(self):
        return json.dumps(self._entities)

    def makeup_question_signature(self, question):
        return question.title().replace(' ', '')

    def get_action_storing_lesson_slots(self):
        # Returns json encoded string.

        # Returns:
        #   String

        slots = self.generate_slots()

        return json.dumps(slots)

    def stringify_action_initialing_slots(self):
        # Returns json encoded string.

        # Returns:
        #   String

        lesson_progress = '{topic}_progress'.format(**{'topic': self.topic})
        slots = self.generate_slots({lesson_progress: 0, 'lesson_topic': self.topic})

        return json.dumps(slots)

    def generate_slots(self, custom={}):
        # Synthesis slots' value based on intrinsic states

        # Parameters:
        #   custom (dict): Overriding or additional information

        # Returns:
        #   dict

        lesson_progress = '{topic}_progress'.format(**{'topic': self.topic})
        slots = {
                lesson_progress: (self.progress + 1),
                'nlu_confused': self.nlu_confused,
                'nlu_confident': self.nlu_confident,
                'will_return': self.will_return,
            }

        if custom:
            for key, value in custom.items():
                slots[key] = value

        return slots

    def transform_to_snake_case(self, text):
        return text.lower().replace(' ', '_')

    def parse_entities(self, random_choice=False):
        if random_choice:
            index = random.randint(0, len(self.utterances) - 1)
        else:
            index = 0
        s = self.utterances[index]
        regex = re.compile(r"\[([\w\s]+)\]\((\w+)\)", re.IGNORECASE)
        matches = regex.findall(s)

        entities = dict()
        for match in matches:
            entities[match[1]] = match[0]

        return entities

    def compile(self):
        # Error
        if self.progress != 0 and not self.is_last:
            template = self.regular_template()
        elif self.progress == 0:
            template = self.initializing_temlate()
        else:
            template = self.finalizing_template()

        return template.render(turn=self)

    def compile_next_checkpoint(self):
        if not self.going_next:
            return '\n'

        tpl = Template("> check_{{ turn.topic }}_{{ turn.progress + 1 }}_{{ turn.going_next }}\n")

        return tpl.render(turn=self)

    def compile_prev_checkpoint(self):
        tpl = Template("> check_{{ turn.topic }}_{{ turn.progress }}_{{ turn.question }}\n")

        return tpl.render(turn=self)

    def regular_template(turn):
        return Template(
                "* {{ turn.intention }}{{ turn.json_entities }}\n"
                "- slot{{ turn.json_entities }}\n"
                "- utter_{{ turn.topic }}_{{ turn.progress + 1 }}_{{ turn.going_next }}\n"
                "- action_store_lesson_history__{{ turn.topic }}\n"
                "- slot{{ turn.json_slots }}\n"
            )

    def initializing_temlate(turn):
        return Template(
                "* client_initialize_{{ turn.topic }}_story\n"
                "- slot{{ turn.stringify_action_initialing_slots() }}\n"
                "- utter_start_{{ turn.topic }}_lesson\n"
                "- utter_{{ turn.topic }}_{{ turn.progress + 1 }}_{{turn.going_next}}\n"
                "- action_store_lesson_history__{{ turn.topic }}\n"
                "- slot{{ turn.json_slots }}\n"
            )

    def finalizing_template(turn):
        return Template(
                "* {{ turn.intention }}{{ turn.json_entities }}\n"
                "- slot{{ turn.json_entities }}\n"
                "- utter_lesson_completed\n"
                "- action_restart\n"
            )


if __name__ == '__main__':
    fpath = dirname(__file__) + '/ministory/a_kiss.yml'
    lesson = Lesson(fpath)
    content = lesson.compile()
    print(content)
