# -*- coding: utf-8 -*-
import re
import logging
# from itertools import islice

from rasa_sdk import Action
# from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    # UserUtteranceReverted,
    # ConversationPaused,
    # EventType,
    FollowupAction,
    # ActionExecuted,
    # UserUttered,
    ActionReverted
)

# from actions import config
# from actions.api.algolia import AlgoliaAPI
# from actions.utils import text_to_float

logger = logging.getLogger(__name__)

answers = [
        "pad-0",
        "he bought a new car",
        "it was a car",
        "it was blue",
        "it was huge",
        "he saw a girl",
        "she was beautiful",
    ]

class ActionInitializeAKissStory(Action):

    def name(self):
        return 'action_initialize_a_kiss_story'

    def run(self, dispatcher, tracker, domain):

        return [SlotSet("lesson_topic", 'a_kiss_story'),
                SlotSet('will_return', None),
                SlotSet("story_progress", 0)]


class ActionStoreLessonHistory__a_kiss(Action):

    def name(self):
        return 'action_store_lesson_history__a_kiss'

    def _extract_question_number(self, action_name):
        p = re.compile(r"_(\d{1,2})_")
        result = p.findall(action_name)

        return int(result[0]) if len(result) > 0 else None

    def run(self, dispatcher, tracker, domain):
        current_state = tracker.current_state()
        logger.debug(f"Current state: {current_state}")

        latest_action_name = tracker.latest_action_name
        question_num = self._extract_question_number(latest_action_name)
        if not question_num:
            return []

        question_num = int(self._extract_question_number(latest_action_name))

        logger.debug(f"latest utterance action: {latest_action_name}")
        logger.debug(f"latest question number: {question_num}")

        return [
                SlotSet('will_return', None),
                SlotSet("story_progress", question_num),
                SlotSet("stm_matched_belief", None),
                SlotSet("stm_unmatched_belief", None),
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
                SlotSet('will_return', "positive"),
                FollowupAction('utter_return_to_previous_question'),
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

        if not question_num:
            raise Exception("Can not get slot value, story_progress")

        return [
                SlotSet("stm_bot_reference_of_truth", answers[question_num]),
                SlotSet('stm_recipient_response', tracker.latest_message['text']),
            ]
