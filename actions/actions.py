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
    ActionExecuted
)

from actions import config
from actions.api.algolia import AlgoliaAPI
from actions.utils import text_to_float

logger = logging.getLogger(__name__)

class ActionInitializeAKissStory(Action):

    def name(self):
        return 'action_initialize_a_kiss_story'

    def run(self, dispatcher, tracker, domain):

        return [SlotSet("lesson_topic", 'a_kiss_story')]

class ActionStoreLessonHistory(Action):

    def name(self):
        return 'action_store_lesson_history'

    def _latest_bot_utter(self, events):
        bot_uters = list(filter(lambda e: e["event"] == "bot", events))
        length = len(bot_uters)

        return bot_uters[length - 1] if length > 0 else None

    def _extract_question_number(self, action_name):
        p = re.compile("_(\d{2})_")
        result = p.findall(action_name)

        return int(result[0]) if len(result) > 0 else None

    def run(self, dispatcher, tracker, domain):
        latest_action_name = tracker.latest_action_name
        question_num = int(self._extract_question_number(latest_action_name))

        if not question_num:
            return []

        logger.debug(f"latest utterance action: {latest_action_name}")
        logger.debug(f"latest question number: {question_num}")

        data = tracker.get_slot("lesson_history")
        if not data:
            data = []
        data.append(question_num)

        return [SlotSet("lesson_history", data), SlotSet("lesson_progress", question_num)]

class ActionTrackingLessonProgress(Action):
    def name(self):
        return 'action_tracking_lesson_progress'

    def run(self, dispatcher, tracker, domain):
        data = tracker.get_slot("lesson_history")
        length = len(data)

        if length == 0:
            return []

        hashed = data[length -1]
        logger.debug(f"lesson progress: hashed value: {hashed}")

        return [SlotSet("lesson_progress", hashed)]

