# -*- coding: utf-8 -*-
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional
from itertool import islice

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

INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_description_mapping.csv"

DIALOGUE_SCRIPT = {
    "a_kiss__answer_1" : {
        "question": ["did carlos by an old car"],
        "answer": ["No, it's a new car"]
        "intent": "a_kiss__answer_1",
        "yes_no": 1,
        "affirmation": 0
    },
    "a_kiss__answer_2" : {
        "question": ["did carlos by an expensive bicycle"],
        "answer": ["I'm afraid you are not correct, it's a car"]
        "intent": "a_kiss__answer_2",
        "yes_no": 1,
        "affirmation": 0
    },
    "a_kiss__answer_3" : {
        "question": ["how big was the car"],
        "intent": "a_kiss__answer_3",
        "yes_no": 0,
        "affirmation": 0
    },
    "a_kiss__answer_4" : {
        "question": ["what color was the car"],
        "intent": "a_kiss__answer_4",
        "yes_no": 0,
        "affirmation": 0
    },
    "a_kiss__answer_6" : {
        "question": ["was the car yellow"],
        "intent": "a_kiss__answer_6",
        "yes_no": 1,
        "affirmation": 0
    },
    "a_kiss__answer_7" : {
        "question": ["when did carlos see a girl on a bicycle"],
        "intent": "a_kiss__answer_7",
        "yes_no": 0,
        "affirmation": 0
    },
    "a_kiss__answer_8" : {
        "question": ["what did she look like"],
        "intent": "a_kiss__answer_8",
        "yes_no": 0,
        "affirmation": 0
    },
    "a_kiss__answer_10" : {
        "question": ["carlos yelled to her. what did he yell"],
        "intent": "a_kiss__answer_10",
        "yes_no": 0,
        "affirmation": 0
    },
    "a_kiss__answer_11" : {
        "question": ["did the girl keep going"],
        "intent": "a_kiss__answer_11",
        "yes_no": 1,
        "affirmation": 1
    },
    "a_kiss__answer_12" : {
        "question": ["where did he want to take her"],
        "intent": "a_kiss__answer_12",
        "yes_no": 0,
        "affirmation": 0
    }
}

class ActionQuestion(Action):
    def __init__(self):
        self.dialogue_script = DIALOGUE_SCRIPT

    def name(self):
        return 'action_question'

    def _filter_user_events(self, events):
        return list(filter(lambda e: e["event"] == "user", events)) 

    def _go_next(latest_intent):
        return next(islice(self.dialogue_script, 1, None), latest_intent)

    def _check_if_intent_answer_correct(latest_intent_name, appropritate_recent_i):
        # get the latest question action
        # get the most recent previous intent

    def _select_message(latest_intent, next_intent):
        if not latest_intent["yes_no"]:
            return next_intent["question"]

        



    def run(self, dispatcher, tracker, domain):

        logging.dedug(tracker.latest_message)

        latest_intent_key = tracker.latest_message['intent']['name']
        latest_intent = self.dialogue_script[latest_intent_key]
        next_intent = self._go_next(latest_intent)
        dispatcher.utter_message(text=DIALOGUE_SCRIPT[intent])
        return []

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents
        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope", "faq", "chitchat"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            button_title = self.get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Something else", "payload": "/trigger_rephrase"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)

class ActionDocsSearch(Action):
    def name(self):
        return "action_docs_search"

    def run(self, dispatcher, tracker, domain):
        docs_found = False
        search_text = tracker.latest_message.get("text")

        # Search of docs pages
        algolia_result = None
        algolia = AlgoliaAPI(
            config.algolia_app_id, config.algolia_search_key, config.algolia_docs_index
        )
        if search_text == "/technical_question{}":
            # If we're in a TwoStageFallback we need to look back one more user utterance
            # to get the actual text
            last_user_event = get_last_event_for(tracker, "user", skip=2)
            if last_user_event:
                search_text = last_user_event.get("text")
                algolia_result = algolia.search(search_text)
        else:
            algolia_result = algolia.search(search_text)

        if (
            algolia_result
            and algolia_result.get("hits")
            and len(algolia_result.get("hits")) > 0
        ):
            docs_found = True
            hits = [
                hit
                for hit in algolia_result.get("hits")
                if "Rasa X Changelog " not in hit.get("hierarchy", {}).values()
                and "Rasa Open Source Change Log "
                not in hit.get("hierarchy", {}).values()
            ]
            if not hits:
                hits = algolia_result.get("hits")
            doc_list = algolia.get_algolia_link(hits, 0)
            doc_list += (
                "\n" + algolia.get_algolia_link(hits, 1)
                if len(algolia_result.get("hits")) > 1
                else ""
            )

            dispatcher.utter_message(
                text="I can't answer your question directly, but I found the following from the docs:\n"
                + doc_list
            )

        else:
            dispatcher.utter_message(
                text=(
                    "I can't answer your question directly, and also "
                    "found nothing in our documentation that would help."
                )
            )

        return [SlotSet("docs_found", docs_found)]

