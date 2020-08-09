## Core thread of scenario
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
    - action_listen
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - slot{"lesson_progress": 1}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - slot{"lesson_progress": 2}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - slot{"lesson_progress": 3}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - action_listen
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - slot{"lesson_progress": 4}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - action_listen
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - slot{"lesson_progress": 5}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - action_listen
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - slot{"lesson_progress": 6}
    - utter_lesson_completed

## Branch 02
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"} OR affirmative__nominalgroup{"nominalgrp": "a new car"}
    - slot{"lesson_progress": 1}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen

## Branch 02 - negative__shortanswer
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer
    - slot{"lesson_progress": 1}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - action_listen

## Branch 03
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - slot{"lesson_progress": 2}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen

## Branch 03 - negative__shortanswer
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer
    - slot{"lesson_progress": 2}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - action_listen

## Branch 04
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - slot{"lesson_progress": 3}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - action_listen

## Branch 05
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue"}
    - slot{"lesson_progress": 4}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - action_listen

## Branch 06
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl"}
    - slot{"lesson_progress": 5}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - action_listen

## Branch 07
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful"}
    - slot{"lesson_progress": 6}
    - utter_lesson_completed

## Branch 07 - affirmative__shortanswer
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer
    - slot{"lesson_progress": 6}
    - utter_lesson_completed
