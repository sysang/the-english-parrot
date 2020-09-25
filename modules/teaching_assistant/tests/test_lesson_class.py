from os.path import dirname

import pytest

from teaching_assistant.main import Lesson


def instantiate_lesson_class():
    fpath = dirname(__file__) + '/files/ministory_script.yml'
    return Lesson(fpath)


class TestLesson:
    def test_get_turn_data(self):
        lesson = instantiate_lesson_class()

        expected = {
                    'progress': 1,
                    'question': "did carlos buy an old car",
                    'scenarios': {
                            'main': {
                                'name': "main",
                                'intention': "nonexclamation__positive__materialpr",
                                'utterances': [
                                    "[he](actor) [bought](materialpr) [a new car](goal)",
                                    "[he](actor) [bought](materialpr) [a new car](goal)",
                                    "[carlos](actor) [bought](materialpr) [a new car](goal)",
                                    "[carlos](actor) [bought](materialpr) [a huge car](goal)",
                                    "[he](actor) [bought](materialpr) [a huge car](goal)",
                                ],
                            },
                    },
                    'going_next': "did carlos buy an expensive bicycle"
            }

        actual = lesson.get_turn_data(expected['progress'])

        assert actual['progress'] == expected['progress']
        assert actual == expected

    def test_get_turn_data__invalid_progress(self):
        lesson = instantiate_lesson_class()
        with pytest.raises(ValueError):
            lesson.get_turn_data(10)
