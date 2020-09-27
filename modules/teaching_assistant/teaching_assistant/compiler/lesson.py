from yaml import load
from yaml import CLoader as Loader

from jinja2 import Environment, PackageLoader

from .dialogue import DialogueTurn
from .constants import Constants
C = Constants()


class Lesson(object):
    def __init__(self, datapath):
        self.env = Environment(loader=PackageLoader('teaching_assistant', 'compiler/templates'))

        self._data = self.ingest_data(datapath)
        self.topic = self._data['topic']
        self.dialogue_turns = self._data['dialogueTurns']
        self.dialogue_length = len(self.dialogue_turns)
        self.scenario_cases = [
                'affirmative__shortanswer',
                'negative__shortanswer',
                'affirmative__adjectivegroup',
                'affirmative__nominalgroup'
            ]

    def ingest_data(self, datapath):
        document = open(datapath)
        parsed = load(document, Loader=Loader)

        return parsed['story']

    def get_turn_data(self, progress):
        for turn in self.dialogue_turns:
            if turn['progress'] == progress:
                return turn

        raise ValueError("Invalid progress value")

    def create_turn(self, data, case):
        return DialogueTurn(
                    topic=self.topic,
                    question=data['question'],
                    scenario_case=data['scenarios'][case]['name'],
                    scenario=data['scenarios'][case],
                    progress=data['progress'],
                    going_next=data['going_next'],
                    is_last=data['progress'] == (self.dialogue_length - 1)
                )

    def compile_main_scenario(self):
        case = C.MAIN_SCENARIO_STR
        content = ''
        for data in self.dialogue_turns:
            turn = self.create_turn(data, case)
            tpl = self.env.get_template('main_scenario.tpl')
            content += tpl.render(turn=turn)

        return content

    def compile_negative_form_scenario(self):
        case = C.NEGATIVE_FORM_SCENARIO_STR
        content = ''
        for data in self.dialogue_turns:
            if case not in data['scenarios']:
                data['scenarios'][C.MAIN_SCENARIO_STR]['name'] = C.NEGATIVE_FORM_SCENARIO_STR
                _case = C.MAIN_SCENARIO_STR
            else:
                _case = case
            turn = self.create_turn(data, _case)
            tpl = self.env.get_template('main_scenario.tpl')
            content += tpl.render(turn=turn)

        return content

    def compile_short_answer_scenario(self):
        content = ''
        for case in self.scenario_cases:
            for data in self.dialogue_turns:
                if case not in data['scenarios']:
                    continue
                turn = self.create_turn(data, case)
                tpl = self.env.get_template('short_answer_scenario.tpl')
                content += tpl.render(turn=turn)

        return content

    def compile_return2previous_quest_scenario(self):
        content = ''
        case = C.MAIN_SCENARIO_STR
        for data in self.dialogue_turns:
            data['scenarios'][C.MAIN_SCENARIO_STR]['name'] = C.RETURN2PREVIOUS_QUEST_SCENARIO_STR
            turn = self.create_turn(data, case)
            tpl = self.env.get_template('return2previous_quest_scenario.tpl')
            content += tpl.render(turn=turn)

        return content

    def compile_cannot_understand_scenario(self):
        content = ''
        case = C.MAIN_SCENARIO_STR
        for data in self.dialogue_turns:
            data['scenarios'][C.MAIN_SCENARIO_STR]['name'] = C.CANNOT_UNDERSTAND_SCENARIO
            turn = self.create_turn(data, case)
            tpl = self.env.get_template('cannot_understand_scenario.tpl')
            content += tpl.render(turn=turn)

        return content
