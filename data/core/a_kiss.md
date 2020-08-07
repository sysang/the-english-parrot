## Scenario - main discussion path
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - action_initialize_a_kiss_story
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "old car"}
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "bicycle"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"}
    - utter_lesson_completed

## Case 1
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "new car"}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "car"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
    - action_listen

## Case 2
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "car"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
    - action_listen

## Case 3
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
    - action_listen

## Case 4
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_tracking_lesson_progress
    - action_listen

## Case 5
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_tracking_lesson_progress
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"}
    - utter_lesson_completed
