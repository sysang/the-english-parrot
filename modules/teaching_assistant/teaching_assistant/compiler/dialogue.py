import json
import re
import random

from jinja2 import Template
from jinja2 import Environment, PackageLoader

from .constants import Constants
C = Constants()


class DialogueTurn(object):
    def __init__(self, topic, question, scenario_case, scenario, progress, going_next, is_last):
        self.env = Environment(loader=PackageLoader('teaching_assistant', 'compiler/templates'))
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
        self.utterances = self.scenario['utterances'] if 'utterances' in self.scenario else []
        self.entities = self.parse_entities()

        self.question = self.makeup_question_signature(self._question)
        self.going_next = self.makeup_question_signature(self._going_next)
        self.topic = self.transform_to_snake_case(topic)
        self.action_slots = self.get_action_storing_lesson_slots()
        self.initial_slots = self.get_action_initialing_slots()

        self.templates = None

    def define_status(self, status=None):
        if status:
            return 'positive'

        return None

    def makeup_question_signature(self, question):
        return question.title().replace(' ', '')

    def transform_to_snake_case(self, text):
        return text.lower().replace(' ', '_')

    def get_action_storing_lesson_slots(self):
        # Returns json encoded string.

        # Returns:
        #   String

        slots = self.generate_slots()

        return slots

    def get_action_initialing_slots(self):
        # Returns json encoded string.

        # Returns:
        #   String

        lesson_progress = '{topic}_progress'.format(**{'topic': self.topic})
        slots = self.generate_slots({lesson_progress: 0, 'lesson_topic': self.topic})

        return slots

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

    def parse_entities(self, random_choice=False):
        if random_choice:
            index = random.randint(0, len(self.utterances) - 1)
        else:
            index = 0

        if len(self.utterances):
            s = self.utterances[index]
            regex = re.compile(r"\[([\w\s]+)\]\((\w+)\)", re.IGNORECASE)
            matches = regex.findall(s)

            entities = dict()
            for match in matches:
                entities[match[1]] = match[0]

            return entities
        else:
            return False

    def compile(self):
        # Error
        template = self.env.get_template('regular_turn.inc')

        return template.render(turn=self)

    def make_templates(self):
        templates = {
                C.MAIN_SCENARIO_STR: self.main_template(),
        }

        return templates

    def compile_next_checkpoint(self):
        tpl = self.env.get_template('next_checkpoint.inc')
        return tpl.render(turn=self)

    def compile_prev_checkpoint(self):
        tpl = self.env.get_template('prev_checkpoint.inc')
        return tpl.render(turn=self)

