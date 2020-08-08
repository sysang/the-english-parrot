## Scenario - main discussion path
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - utter_lesson_completed

## Step 1
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen

## Step 1 - negative__shortanswer
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_initialize_a_kiss_story
    - action_store_lesson_history
    - action_listen
* negative__shortanswer
    - slot{"lesson_progress": 1}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen

## Step 2
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen

## Step 2 - negative__shortanswer
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen
* negative__shortanswer
    - slot{"lesson_progress": 2}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen

## Step 3
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - slot{"lesson_progress": 11913.539627075195}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - action_listen

## Step 4
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - action_listen

## Step 5
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - action_listen

## Step 6
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - action_listen
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - utter_lesson_completed

## Step 6 - affirmative__shortanswer
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - action_listen
* affirmative__shortanswer
    - slot{"lesson_progress": 6}
    - utter_lesson_completed
