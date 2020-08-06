# -*- coding: utf-8 -*-
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional

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

        return [SlotSet("lesson_topic", 'a_kiss_story')]

class ActionTrackingProgress(Action):

    def name(self):
        return 'action_tracking_lesson_progress'

    def run(self, dispatcher, tracker, domain):
        latest_intent = tracker.latest_message['intent']['name']

        return [SlotSet("lesson_progress", latest_intent)]
