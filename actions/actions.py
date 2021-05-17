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
    UserUttered
)

# from actions import config
# from actions.api.algolia import AlgoliaAPI
# from actions.utils import text_to_float

logger = logging.getLogger(__name__)


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

        return [SlotSet('will_return', None),
                SlotSet("story_progress", question_num)]


class ActionNotSureWhatToDoFallback(Action):
    def name(self):
        return 'action_not_sure_what_to_do_fallback'

    def run(self, dispatcher, tracker, domain):

        return [SlotSet('will_return', "positive")]
