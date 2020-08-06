## Scenario - main discussion path
* client_initializes_a_kiss_story
    - action_initialize_a_kiss_story
    - utter_introduce_lesson
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "new car"}
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_tracking_lesson_progress
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "car"}
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_question_HowBigWasCar
    - action_tracking_lesson_progress
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR nonexclamation__positive__materialpr{"actor": "he", "meterialpr": "bought", "goal": "huge car"}
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_question_WhatColorWasCar
    - action_tracking_lesson_progress
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"}
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_tracking_lesson_progress
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"}
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_lesson_completed
    - action_initialize_a_kiss_story
    - utter_introduce_lesson
