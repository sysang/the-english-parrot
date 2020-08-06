# -*- coding: utf-8 -*-
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
)

from actions import config
from actions.api.algolia import AlgoliaAPI

logger = logging.getLogger(__name__)

class ActionInitializeAKissStory(Action):

    def name(self):
        return 'action_initialize_a_kiss_story'

    def run(self, dispatcher, tracker, domain):
        [SlotSet("lesson_progress", "")]
        [SlotSet("lesson_topic", 'a_kiss_story')]

        return

class ActionTrackingProgress(Action):

    def name(self):
        return 'action_tracking_lesson_progress'

    def _latest_bot_utter(self, events):
        bot_uters = list(filter(lambda e: e["event"] == "bot", events))
        length = len(bot_uters)

        return bot_uters[length - 1] if length > 0 else None

    def run(self, dispatcher, tracker, domain):
        latest_bot_utterance = self._latest_bot_utter(tracker.events)
        logger.debug(f"latest bot utterance: {latest_bot_utterance}")

        if not latest_bot_utterance:
            return

        return [SlotSet("lesson_progress", latest_bot_utterance['text'])]
