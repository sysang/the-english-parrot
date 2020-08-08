## Scenario - main discussion path
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.22335615404881537}
    - utter_a_kiss_question_HowBigWasCar
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.18178618815727532}
    - utter_a_kiss_question_WhatColorWasCar
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.19618684938177466}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.2911441989708692}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - slot{"lesson_progress": 0.19111480936408043}
    - utter_lesson_completed

## Step 1
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - action_initialize_a_kiss_story
    - action_tracking_lesson_progress
    - slot{"lesson_topic": "a_kiss_story", "lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_listen

## Step 1 - negative__shortanswer
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - action_initialize_a_kiss_story
    - action_listen
* negative__shortanswer
    - action_initialize_a_kiss_story
    - action_tracking_lesson_progress
    - slot{"lesson_topic": "a_kiss_story", "lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_listen

## Step 2
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.22335615404881537}
    - utter_a_kiss_question_HowBigWasCar
    - action_listen

## Step 2 - negative__shortanswer
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.5761540986131877}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - action_listen
* negative__shortanswer
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.22335615404881537}
    - utter_a_kiss_question_HowBigWasCar
    - action_listen

## Step 3
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.22335615404881537}
    - utter_a_kiss_question_HowBigWasCar
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.18178618815727532}
    - utter_a_kiss_question_WhatColorWasCar
    - action_listen

## Step 4
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.18178618815727532}
    - utter_a_kiss_question_WhatColorWasCar
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.19618684938177466}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_listen

## Step 5
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.19618684938177466}
    - utter_a_kiss_question_WhileDrivingDownWhatDidHeSee
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.2911441989708692}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_listen

## Step 6
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - action_tracking_lesson_progress
    - slot{"lesson_progress": 0.2911441989708692}
    - utter_a_kiss_question_DidSheLookBeautiful
    - action_listen
* affirmative__shortanswer
    - slot{"lesson_progress": 0.19111480936408043}
    - utter_lesson_completed
