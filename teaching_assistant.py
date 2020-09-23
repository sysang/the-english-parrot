from yaml import load
from yaml import CLoader as Loader
import json
from jinja2 import Template

from devutils import showlist

file = open('lectures/ministory/a_kiss.yml')
lesson = load(file, Loader=Loader)


class DialogueTurn(object):
    def __init__(self, lesson, scenario, progress, intention, entities, question):
        self._question = question
        self._entities = entities
        self._lesson = lesson
        self.scenario = scenario
        self.lesson = self.transform_to_snake_case(lesson)
        self.progress = progress
        self.intention = intention
        self.entities = self.json_stringify_entities()
        self.question = self.make_question_signature()
        self.slots = self.generate_slot_values()

    def json_stringify_entities(self):
        return json.dumps(self._entities)

    def make_question_signature(self):
        return self._question.title().replace(' ', '')

    def generate_slot_values(self):
        s = '{{"{lesson}_progress": {progress}, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}}'
        data = {'lesson': self.lesson, 'progress': self.progress}

        return s.format(**data)

    def transform_to_snake_case(self, text):
        return text.lower().replace(' ', '_')


def dialogue_turn_content(turn):
    template = Template(
            "* {{ turn.intention }}{{ turn.entities }}\n"
            "- slot{{ turn.entities }}\n"
            "- utter_{{ turn.lesson }}_{{turn.progress}}_{{turn.question}}\n"
            "- action_store_lesson_history__{{ turn.lesson }}\n"
            "- slot{{ turn.slots }}\n"
            "> check_{{ turn.lesson }}_{{turn.progress}}_{{turn.question}}\n"
        )

    return template.render(turn=turn)


turn = DialogueTurn(
            lesson='a kiss',
            scenario='main',
            progress=2,
            intention='nonexclamation__positive__materialpr',
            entities={"actor": "he", "materialpr": "bought", "goal": "a new car"},
            question="did carlos buy an expensive car"
        )

content = dialogue_turn_content(turn)
print(content)

