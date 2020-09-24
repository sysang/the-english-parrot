from yaml import load
from yaml import CLoader as Loader
import json
import re
import random
from jinja2 import Template

from devutils import showlist


class Lesson(object):
    def __init__(self, datapath):
        self._data = self.ingest_data(datapath)
        self.topic = self._data['topic']
        self.dialogue_turns = self._data['dialogueTurns']
        self.dialogue_lenth = len(self.dialogueTurns)

    def ingest_data(self, datapath):
        file = open(datapath)
        parsed = load(file, Loader=Loader)

        return parsed['story']

    def get_turn_data(self, progres):
        pass

    def create_turn(self, progress):
        pass

    def create_check_point(self, progress):
        pass


class DialogueTurn(object):
    def __init__(self, topic, scenario, progress, intention, utterances, question):
        self.nlu_confused = None
        self.nlu_confident = self.define_status(True)  # 'positive' or None because any value except None will be treated as 1 (True)
        self.will_return = None

        self._question = question
        self._topic = topic
        self.utterances = utterances
        self.scenario = scenario
        self.progress = progress
        self.intention = intention

        self.topic = self.transform_to_snake_case(topic)
        self.entities = self.parse_entities()
        self.question = self.makeup_question_signature()
        self.slots = self.get_action_storing_lesson_slots()

    def define_status(self, status=None):
        if status:
            return 'positive'

        return None

    def json_stringify_entities(self):
        return json.dumps(self._entities)

    def makeup_question_signature(self):
        return self._question.title().replace(' ', '')

    def get_action_storing_lesson_slots(self):
        return self.json_stringify_slot_values()

    def get_action_initialing_slots(self):
        return self.json_stringify_slot_values({'progress': 0, 'lesson_topic': self.topic})

    def json_stringify_slot_values(self, custom={}):
        lesson_progress = '{topic}_progress'.format(**{'topic': self.topic})
        data = {
                lesson_progress: self.progress if 'progress' not in custom else custom['progress'],
                'nlu_confused': self.nlu_confused if 'nlu_confused' not in custom else custom['nlu_confused'],
                'nlu_confident': self.nlu_confident if 'nlu_confident' not in custom else custom['nlu_confident'],
                'will_return': self.will_return if 'will_return' not in custom else custom['will_return'],
            }

        if custom:
            for key, value in custom.items():
                data[key] = value

        return json.dumps(data)

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

        return json.dumps(entities)


def dialogue_turn_content(turn):
    template = Template(
            "* {{ turn.intention }}{{ turn.entities }}\n"
            "- slot{{ turn.entities }}\n"
            "- utter_{{ turn.topic }}_{{turn.progress}}_{{turn.question}}\n"
            "- action_store_lesson_history__{{ turn.topic }}\n"
            "- slot{{ turn.slots }}\n"
            "> check_{{ turn.lesson }}_{{turn.progress}}_{{turn.question}}\n"
        )

    return template.render(turn=turn)


def dialogue_initialize_lesson(turn):
    template = Template(
            "* client_initialize_{{ turn.topic }}_story\n"
            "- slot{{ turn.get_action_initialing_slots() }}\n"
            "- utter_start_{{ turn.lesson }}_lesson\n"
            "- utter_{{ turn.topic }}_{{turn.progress}}_{{turn.question}}\n"
            "- action_store_lesson_history__{{ turn.topic }}\n"
            "- slot{{ turn.slots }}\n"
            "> check_{{ turn.lesson }}_{{turn.progress}}_{{turn.question}}\n"
        )

    return template.render(turn=turn)


def dialogue_finalize_lesson(turn):
    template = Template(
            "* {{ turn.intention }}{{ turn.entities }}\n"
            "- slot{{ turn.entities }}\n"
            "- utter_lesson_completed\n"
            "- action_restart\n"
        )

    return template.render(turn=turn)


def compile_story():
    file = open('lectures/ministory/a_kiss.yml')
    parsed = load(file, Loader=Loader)
    story = parsed['story']
    topic = story['topic']
    dialogue_turns = story['dialogueTurns']
    dialogue_lenth = len(dialogue_turns)

    content = ''
    for instruction in dialogue_turns:
        turn = DialogueTurn(
                    topic=topic,
                    scenario=instruction['scenario']['main']['name'],
                    progress=instruction['progress'],
                    intention=instruction['scenario']['main']['intention'],
                    utterances=instruction['scenario']['main']['utterances'],
                    question=instruction['going_next']
                )

        if instruction['progress'] != 0 and instruction['progress'] != (dialogue_lenth - 1):
            turn = dialogue_turn_content(turn)
        elif instruction['progress'] == 0:
            turn = dialogue_initialize_lesson(turn)
        else:
            turn = dialogue_finalize_lesson(turn)

        content += '\n' + turn

    return content


if __name__ == '__main__':
    content = compile_story()
    print(content)
