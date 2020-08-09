## Core thread of scenario
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"lesson_progress": 1, "actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"lesson_progress": 1, "actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"lesson_progress": 1, "nominalgrp": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"lesson_progress": 2, "identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"lesson_progress": 1, "identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"lesson_progress": 1, "nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"lesson_progress": 3, "carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"lesson_progress": 3, "adjectivegrp": "huge"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"lesson_progress": 4, "carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"lesson_progress": 4, "adjectivegrp": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"lesson_progress": 5, "senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"lesson_progress": 5, "nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"lesson_progress": 6, "carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"lesson_progress": 6, "adjectivegrp": "beautiful"}
    - utter_lesson_completed

## Branch 02
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"lesson_progress": 1, "actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"lesson_progress": 1, "actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"lesson_progress": 1, "nominalgrp": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history

## Branch 02 - negative__shortanswer
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer{"lesson_progress": 1}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history

## Branch 03
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"lesson_progress": 1, "identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"lesson_progress": 1, "identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"lesson_progress": 1, "nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history

## Branch 03 - negative__shortanswer
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer{"lesson_progress": 2}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history

## Branch 04
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"lesson_progress": 3, "carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"lesson_progress": 3, "adjectivegrp": "huge"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history

## Branch 05
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"lesson_progress": 4, "carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"lesson_progress": 4, "adjectivegrp": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history

## Branch 06
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"lesson_progress": 5, "senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"lesson_progress": 5, "nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history

## Branch 07
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"lesson_progress": 6, "carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"lesson_progress": 6, "adjectivegrp": "beautiful"}
    - utter_lesson_completed

## Branch 07 - affirmative__shortanswer
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer{"lesson_progress": 6}
    - utter_lesson_completed
