from os.path import dirname

from teaching_assistant.compiler import Lesson


if __name__ == '__main__':
    fpath = dirname(__file__) + '/ministory/a_kiss.yml'
    lesson = Lesson(fpath)
    content = lesson.compile_main_scenario()
    content += lesson.compile_negative_form_scenario()
    content += lesson.compile_short_answer_scenario()
    content += lesson.compile_cannot_understand_scenario()
    content += lesson.compile_return2previous_quest_scenario()
    print(content)
