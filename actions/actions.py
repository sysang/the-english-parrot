# -*- coding: utf-8 -*-
import re
import logging
# from itertools import islice

from rasa_sdk import Action
# from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    BotUttered,
    FollowupAction,
    # UserUtteranceReverted,
    # ConversationPaused,
    # EventType,
    # ActionExecuted,
    # ActionReverted
)

# from actions import config
# from actions.api.algolia import AlgoliaAPI
# from actions.utils import text_to_float

logger = logging.getLogger(__name__)

A_KISS_STORY = [
        {},
        {
            'truth': "he bought a new car",
            'axis': 'goal'
        },
        {
            'truth': "he bought a expensive car",
            'axis': 'goal'
        },
        {
            'truth': "it was huge",
            'axis': 'attribute'
        },
        {
            'truth': "it was blue",
            'axis': 'attribute'
        },
        {
            'truth': "he saw a girl",
            'axis': 'phenomenon'
        },
        {
            'truth': "she looked beautiful",
            'axis': 'attribute'
        },
    ]

ANSWERS = {
        "a_kiss_story": A_KISS_STORY,
    }

QUESTIONS = {
    'a_kiss_story': [
        "in this lesson i will ask many questions. you must answer every question.  okay. let's start the story. a kiss...",
        "did carlos buy an old car",
        "did carlos buy an expensive bicycle",
        "how big is the car",
        "what color was the car",
        "while driving down the street. what did he see",
        "did she look beautiful",
        "that's all. you did a very good job",
    ]
}

UTTERANCES = {
    'inform_incorrect_answer': "it is not correct"
}


def query_reference_of_truth(story, question_num):
    return ANSWERS[story][question_num]


def query_bot_utterance(story, question_num):
    story_questions = QUESTIONS[story]

    if (question_num >= len(story_questions)):
        return None

    return story_questions[question_num]


class ActionInitializeAKissStory(Action):

    def name(self):
        return 'action_initialize_a_kiss_story'

    def run(self, dispatcher, tracker, domain):

        story_progress = 0
        topic = 'a_kiss_story'

        utterance = query_bot_utterance(topic, story_progress)

        return [
                SlotSet("lesson_topic", topic),
                SlotSet('will_return', None),
                SlotSet("story_progress", story_progress),
                BotUttered(text=utterance),
            ]


class ActionProceedDialogue(Action):

    def name(self):
        return 'action_proceed_dialogue'

    def run(self, dispatcher, tracker, domain):

        story = tracker.get_slot('lesson_topic')
        logger.debug(f"query quesion for story: {story}")

        story_progress = tracker.get_slot('story_progress')
        logger.debug(f"latest question number: {story_progress}")

        stm_matched_belief = tracker.get_slot('stm_matched_belief')
        stm_unmatched_belief = tracker.get_slot('stm_unmatched_belief')

        if not stm_matched_belief and not stm_unmatched_belief:
            raise Exception("There might be a breach in training data leading this bad perceptional state.")

        question_num = story_progress + 1

        if stm_matched_belief:
            question = query_bot_utterance(story, question_num)

            return [
                SlotSet('story_progress', question_num),
                BotUttered(text=question)
            ]

        elif stm_unmatched_belief:
            inform_utterance = UTTERANCES['inform_incorrect_answer']
            answer = query_reference_of_truth(story, story_progress)

            question = query_bot_utterance(story, question_num)

            return [
                SlotSet('story_progress', question_num),
                BotUttered(text=inform_utterance),
                BotUttered(text=answer),
                BotUttered(text=question),
            ]


class ActionFinalizeBotDialogueTurn(Action):

    def name(self):
        return 'action_finalize_bot_dialogue_turn'

    def _extract_question_number(self, action_name):
        p = re.compile(r"_(\d{1,2})_")
        result = p.findall(action_name)

        return int(result[0]) if len(result) > 0 else None

    def run(self, dispatcher, tracker, domain):
        current_state = tracker.current_state()
        logger.debug(f"Current state: {current_state}")

        latest_action_name = tracker.latest_action_name
        logger.debug(f"latest utterance action: {latest_action_name}")

        question_num = tracker.get_slot('story_progress')
        logger.debug(f"latest question number: {question_num}")

        return [
            SlotSet('will_return', None),
            SlotSet("stm_matched_belief", None),
            SlotSet("stm_unmatched_belief", None),
            SlotSet('stm_recipient_response', None),
            SlotSet('stm_bot_reference_of_truth', None),
            SlotSet('stm_semantic_axis', None),
            SlotSet("materialpr", None),
            SlotSet("actor", None),
            SlotSet("goal", None),
            SlotSet("scope", None),
            SlotSet("beneficiary", None),
            SlotSet("attributivepr", None),
            SlotSet("carrier", None),
            SlotSet("attribute", None),
            SlotSet("identifyingpr", None),
            SlotSet("identified", None),
            SlotSet("identifier", None),
            SlotSet("mentalpr", None),
            SlotSet("senser", None),
            SlotSet("phenomenon", None),
            SlotSet("behaviouralpr", None),
            SlotSet("behaver", None),
            SlotSet("verbalpr", None),
            SlotSet("sayer", None),
            SlotSet("reciver", None),
            SlotSet("verbiage", None),
            SlotSet("existantialpr", None),
            SlotSet("existent", None),
            SlotSet("nominalgrp", None),
            SlotSet("adjectivegrp", None),
            SlotSet("prepositionallocation", None),
        ]


class ActionNotSureWhatToDoFallback(Action):
    def name(self):
        return 'action_not_sure_what_to_do_fallback'

    def run(self, dispatcher, tracker, domain):

        return [
            SlotSet('stm_matched_belief', None),
            SlotSet('stm_unmatched_belief', None),
            SlotSet('stm_recipient_response', None),
            SlotSet('stm_bot_reference_of_truth', None),
            SlotSet('stm_semantic_axis', None),
            SlotSet('will_return', "positive"),
            SlotSet("materialpr", None),
            SlotSet("actor", None),
            SlotSet("goal", None),
            SlotSet("scope", None),
            SlotSet("beneficiary", None),
            SlotSet("attributivepr", None),
            SlotSet("carrier", None),
            SlotSet("attribute", None),
            SlotSet("identifyingpr", None),
            SlotSet("identified", None),
            SlotSet("identifier", None),
            SlotSet("mentalpr", None),
            SlotSet("senser", None),
            SlotSet("phenomenon", None),
            SlotSet("behaviouralpr", None),
            SlotSet("behaver", None),
            SlotSet("verbalpr", None),
            SlotSet("sayer", None),
            SlotSet("reciver", None),
            SlotSet("verbiage", None),
            SlotSet("existantialpr", None),
            SlotSet("existent", None),
            SlotSet("nominalgrp", None),
            SlotSet("adjectivegrp", None),
            SlotSet("prepositionallocation", None),
            FollowupAction('utter_return_to_previous_question'),
        ]


class ActionRepeatLastUtterance(Action):
    def name(self):
        return 'action_repeat_last_utterance'

    def run(self, dispatcher, tracker, domain):

        story_progress = tracker.get_slot('story_progress')
        logger.debug(f"latest question number: {story_progress}")

        utterance = query_bot_utterance(story, story_progress)

        return [
                BotUttered(text=utterance),
            ]



class ActionActivateMatchedPerception(Action):
    def name(self):
        return 'action_activate_matched_perception'

    def run(self, dispatcher, tracker, domain):

        return [
                SlotSet('stm_matched_belief', True),
            ]


class ActionActivateUnMatchedPerception(Action):
    def name(self):
        return 'action_activate_unmatched_perception'

    def run(self, dispatcher, tracker, domain):

        return [
                SlotSet('stm_unmatched_belief', True),
            ]


class ActionMemorizeUserResponse(Action):
    def name(self):
        return 'action_memorize_user_response'

    def run(self, dispatcher, tracker, domain):

        question_num = tracker.get_slot('story_progress')
        story = tracker.get_slot('lesson_topic')

        if not question_num:
            raise Exception("Can not get slot value, story_progress")

        answer = query_reference_of_truth(story, question_num)

        return [
                SlotSet('stm_recipient_response', tracker.latest_message['text']),
                SlotSet("stm_bot_reference_of_truth", answer['truth']),
                SlotSet("stm_semantic_axis", answer['axis']),
            ]
