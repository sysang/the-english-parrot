## Scenario - main discussion path
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - action_initialize_a_kiss_story
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - utter_lesson_completed

## Case 1
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - action_initialize_a_kiss_story
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_tracking_lesson_progress
    - action_listen

## Case 2
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
    - action_listen

## Case 3
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
    - action_listen

## Case 4
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
    - action_listen

## Case 5
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_tracking_lesson_progress
    - action_listen

## Case 6
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - utter_lesson_completed
