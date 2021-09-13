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
        {
            'truth': "the english parrot initializes a kiss story",
            'axis': 'goal'
        },
        {
            'truth': "he bought a new car",
            'axis': 'goal'
        },
        {
            'truth': "he bought an expensive car",
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

UTTERANCES = {
    'a_kiss_story': [
        "in this lesson i will ask many questions. you must answer every question.  okay. let's start the story. a kiss...",
        "did carlos buy an old car",
        "did carlos buy an expensive bicycle",
        "how big is the car",
        "what color was the car",
        "while driving down the street. what did he see",
        "did she look beautiful",
        "that's all. you did a very good job",
    ],
    'inform_incorrect_answer': ["it is not correct"]
}


class ActionCommon():

    def get_story_progress_slot(self, dispatcher, tracker, domain):

        story_progress = tracker.get_slot('story_progress')
        logger.debug(f"latest question number: {story_progress}")

        if story_progress is None:
            raise Exception("Can not get slot value, story_progress")

        return story_progress

    def get_dialogue_topic_slot(self, dispatcher, tracker, domain):
        story_progress = self.get_story_progress_slot(dispatcher, tracker, domain)

        if story_progress == 0:

            entities = tracker.latest_message['entities']
            goal_entity = [e for e in entities if e['entity'] == 'goal']
            if not len(goal_entity):
                raise Exception("Fatar error: story topic can not be retrieved!")

            topic = goal_entity[0]['value']
            topic = "_".join(topic.split())

        else:
            topic = tracker.get_slot('dialogue_topic')

        logger.debug(f"query quesion for topic: {topic}")

        return topic

    def query_reference_of_truth(self, topic, question_num):
        return ANSWERS[topic][question_num]

    def query_story(self, topic):
        return {
            'answers': ANSWERS[topic]
        }

    def query_bot_utterance(self, topic, question_num):
        story_questions = UTTERANCES[topic]

        if (question_num >= len(story_questions)):
            return None

        return story_questions[question_num]

    def create_event_reseting_entity_slots(self):

        return [
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
            SlotSet("negativenominalgrp", None),
            SlotSet("adjectivegrp", None),
            SlotSet("negativeadjectivegrp", None),
            SlotSet("adjectivegrp", None),
            SlotSet("prepositionallocation", None),
            SlotSet("negative", None),
            SlotSet("affirmative", None),
        ]

class ActionProceedDialogue(Action, ActionCommon):

    def name(self):
        return 'action_proceed_dialogue'

    def run(self, dispatcher, tracker, domain):
        # current_state = tracker.current_state()
        # logger.debug(f"Current state: {current_state}")

        # latest_action_name = tracker.latest_action_name
        # logger.debug(f"latest utterance action: {latest_action_name}")

        topic = self.get_dialogue_topic_slot(dispatcher, tracker, domain)

        story_progress = tracker.get_slot('story_progress')
        logger.debug(f"latest story progress: {story_progress}")

        stm_matched_belief = tracker.get_slot('stm_matched_belief')
        stm_unmatched_belief = tracker.get_slot('stm_unmatched_belief')

        if not stm_matched_belief and not stm_unmatched_belief:
            raise Exception("There might be a breach in training data leading bad perceptional states.")

        if story_progress == 0:

            utterance = self.query_bot_utterance(topic, story_progress)

            events = [
                    SlotSet('intent_rephrase', None),
                    SlotSet("story_end", None),
                    BotUttered(text=utterance),
                ]
        else:
            events = []

        progress_next = story_progress + 1

        events.append(SlotSet('story_progress', progress_next))
        events.append(SlotSet("stm_matched_belief", None))
        events.append(SlotSet("stm_unmatched_belief", None))

        if stm_unmatched_belief:
            inform_utterance = UTTERANCES['inform_incorrect_answer'][0]
            answer = self.query_reference_of_truth(topic, story_progress)

            events.append(BotUttered(text=inform_utterance))
            events.append(BotUttered(text=answer['truth']))

        answers = self.query_story(topic)['answers']
        question = self.query_bot_utterance(topic, progress_next)
        if progress_next < len(answers):
            events.append(SlotSet('stm_bot_verbal_intention', question))
            events.append(SlotSet("bot_intent_listen", True))
            events.append(SlotSet('story_end', False))
        else:
            events.append(SlotSet('stm_bot_verbal_intention', None))
            events.append(SlotSet("bot_intent_listen", None))
            events.append(SlotSet('story_end', True))

        events.append(BotUttered(text=question))

        return events


class ActionEndStory(Action):

    def name(self):
        return 'action_end_story'

    def run(self, dispatcher, tracker, domain):

        return [
            FollowupAction('action_restart'),
        ]

class ActionFinalizeBotDialogueTurn(Action):

    def name(self):
        return 'action_finalize_bot_dialogue_turn'

    def run(self, dispatcher, tracker, domain):

        return [
        ]


class ActionHanleListen(Action):
    def name(self):
        return 'action_handle_listen'

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("bot_intent_listen", None),
            FollowupAction('action_listen'),
        ]


class ActionMemorizeUserResponse(Action, ActionCommon):
    def name(self):
        return 'action_memorize_user_response'

    def run(self, dispatcher, tracker, domain):

        story_progress = self.get_story_progress_slot(dispatcher, tracker, domain)
        topic = self.get_dialogue_topic_slot(dispatcher, tracker, domain)

        if story_progress == 0:
            events = [
                SlotSet("dialogue_topic", topic),
            ]
        else:
            events = []

        answer = self.query_reference_of_truth(topic, story_progress)

        return [
                SlotSet('stm_recipient_response', tracker.latest_message['text']),
                SlotSet("stm_bot_reference_of_truth", answer['truth']),
                SlotSet("stm_semantic_axis", answer['axis']),
            ] + events


class ActionActivateMatchedPerception(Action, ActionCommon):
    def name(self):
        return 'action_activate_matched_perception'

    def run(self, dispatcher, tracker, domain):

        return [
                SlotSet('stm_matched_belief', True),
                SlotSet('stm_unmatched_belief', None),
                SlotSet('stm_bot_verbal_intention', None),
                SlotSet('stm_recipient_response', None),
                SlotSet('stm_bot_reference_of_truth', None),
                SlotSet('stm_semantic_axis', None),
            ] + self.create_event_reseting_entity_slots()


class ActionActivateUnMatchedPerception(Action, ActionCommon):

    def name(self):
        return 'action_activate_unmatched_perception'

    def run(self, dispatcher, tracker, domain):

        return [
                SlotSet('stm_unmatched_belief', True),
                SlotSet('stm_matched_belief', None),
                SlotSet('stm_bot_verbal_intention', None),
                SlotSet('stm_recipient_response', None),
                SlotSet('stm_bot_reference_of_truth', None),
                SlotSet('stm_semantic_axis', None),
            ] + self.create_event_reseting_entity_slots()


class ActionNotSureWhatToDoFallback(Action, ActionCommon):

    def name(self):
        return 'action_not_sure_what_to_do_fallback'

    def run(self, dispatcher, tracker, domain):

        return [
            SlotSet('intent_rephrase', True),
            SlotSet('stm_matched_belief', None),
            SlotSet('stm_unmatched_belief', None),
            SlotSet('stm_bot_verbal_intention', None),
            SlotSet('stm_recipient_response', None),
            SlotSet('stm_bot_reference_of_truth', None),
            SlotSet('stm_semantic_axis', None),
        ] + self.create_event_reseting_entity_slots() + [FollowupAction('utter_return_to_previous_question')]


class ActionRepeatLastUtterance(Action, ActionCommon):

    def name(self):
        return 'action_repeat_last_utterance'

    def run(self, dispatcher, tracker, domain):

        topic = self.get_dialogue_topic_slot(dispatcher, tracker, domain)
        story_progress = self.get_story_progress_slot(dispatcher, tracker, domain)

        if story_progress == 0:
            return []

        utterance = self.query_bot_utterance(topic, story_progress)

        return [
                BotUttered(text=utterance),
                SlotSet('intent_rephrase', None),
                SlotSet("bot_intent_listen", True),
            ]
