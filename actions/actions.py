# -*- coding: utf-8 -*-
import re
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional
from itertools import islice

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
    ActionExecuted,
    UserUttered
)

from actions import config
# from actions.api.algolia import AlgoliaAPI
from actions.utils import text_to_float

logger = logging.getLogger(__name__)

class ActionInitializeAKissStory(Action):

    def name(self):
        return 'action_initialize_a_kiss_story'

    def run(self, dispatcher, tracker, domain):

        return [SlotSet("lesson_topic", 'a_kiss_story'), SlotSet('nlu_confused', None), SlotSet('nlu_confident', 'positive'), SlotSet('will_return', None), SlotSet("lesson_history", []), SlotSet("a_kiss_progress", 0)]

class ActionStoreLessonHistory__a_kiss(Action):

    def name(self):
        return 'action_store_lesson_history__a_kiss'

    def _extract_question_number(self, action_name):
        p = re.compile("_(\d{2})_")
        result = p.findall(action_name)

        return int(result[0]) if len(result) > 0 else None

    def run(self, dispatcher, tracker, domain):
        latest_action_name = tracker.latest_action_name

        question_num = self._extract_question_number(latest_action_name)
        if not question_num:
            return []

        question_num = int(self._extract_question_number(latest_action_name))

        logger.debug(f"latest utterance action: {latest_action_name}")
        logger.debug(f"latest question number: {question_num}")

        data = tracker.get_slot("lesson_history")
        if not data:
            data = []
        data.append(question_num)

        return [SlotSet('nlu_confused', None), SlotSet('nlu_confident', 'positive'), SlotSet('will_return', None), SlotSet("lesson_history", data), SlotSet("a_kiss_progress", question_num)]

class ActionNotUnderstandFallback(Action):
    def name(self):
        return 'action_not_understand_fallback'

    def run(self, dispatcher, tracker, domain):

        return [SlotSet("nlu_confused", "positive"), SlotSet('nlu_confident', None), FollowupAction('utter_can_not_understand')]

class ActionNotSureWhatToDoFallback(Action):
    def name(self):
        return 'action_not_sure_what_to_do_fallback'

    def _latest_user_uttered(self, events) -> UserUttered:
        utters = list(filter(lambda e: e["event"] == "user", events))
        length = len(utters)

        if length <= 0:
            return None

        latest_user_utter_data = self._latest_user_utter(events)

        user_uttered = UserUttered(
                text=latest_user_utter_data['text'],
                parse_data=latest_user_utter_data['parse_data'],
                input_channel=latest_user_utter_data['input_channel']
                )

        return user_uttered

    def run(self, dispatcher, tracker, domain):
        # events = tracker.current_state()['events']

        return [FollowupAction('utter_return_to_previous_question'), SlotSet('will_return', "positive")]

class ActionInitializeChangedStory(Action):

    def name(self):
        return 'action_initialize_changed_story'

    def run(self, dispatcher, tracker, domain):

        return [SlotSet("lesson_topic", 'changed_story'), SlotSet('nlu_confused', None), SlotSet('nlu_confident', 'positive'), SlotSet('will_return', None), SlotSet("lesson_history", []), SlotSet("changed_progress", 0)]

class ActionStoreLessonHistory__changed(Action):

    def name(self):
        return 'action_store_lesson_history__changed'

    def _extract_question_number(self, action_name):
        p = re.compile("_(\d{2})_")
        result = p.findall(action_name)

        return int(result[0]) if len(result) > 0 else None

    def run(self, dispatcher, tracker, domain):
        latest_action_name = tracker.latest_action_name

        question_num = self._extract_question_number(latest_action_name)
        if not question_num:
            return []

        question_num = int(self._extract_question_number(latest_action_name))

        logger.debug(f"latest utterance action: {latest_action_name}")
        logger.debug(f"latest question number: {question_num}")

        data = tracker.get_slot("lesson_history")
        if not data:
            data = []
        data.append(question_num)

        return [SlotSet('nlu_confused', None), SlotSet('nlu_confident', 'positive'), SlotSet('will_return', None), SlotSet("lesson_history", data), SlotSet("changed_progress", question_num)]
