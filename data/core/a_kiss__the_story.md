## Core thread of scenario
* client_initializes_a_kiss_story
    - action_initialize_a_kiss_story
    - slot{"a_kiss_progress": 0, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_start_a_kiss_lesson
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "nlu_confident": "positive", "actor": "he", "materialpr": "bought", "goal": "a new car", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "nlu_confident": "positive", "actor": "he", "materialpr": "buy", "goal": "an old car", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"a_kiss_progress": 2, "nlu_confident": "positive", "identified": "it","identifier": "a car", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "nlu_confident": "positive", "identified": "it", "identifier": "a bicycle", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confident": "positive", "carrier": "it","attribute": "huge", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confident": "positive", "carrier": "it", "attribute": "blue", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confident": "positive", "senser": "he","mentalpr": "saw", "phenomenon": "a girl", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "nlu_confident": "positive", "carrier": "she", "attribute": "beautiful", "lesson_topic": "a_kiss_story"}
    - utter_lesson_completed
    - action_restart

## Scenario of short answers - 01
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer{"a_kiss_progress": 1, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of short answers - 02
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer{"a_kiss_progress": 2, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of short answers - 03
> check_a_kiss_03_HowBigWasCar
* affirmative__adjectivegroup{"a_kiss_progress": 3, "nlu_confident": "positive", "adjectivegrp": "huge", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of short answers - 04
> check_a_kiss_04_WhatColorWasCar
* affirmative__adjectivegroup{"a_kiss_progress": 4, "nlu_confident": "positive", "adjectivegrp": "blue", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of short answers - 04
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* affirmative__nominalgroup{"a_kiss_progress": 5, "nlu_confident": "positive", "nominalgrp": "a girl", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of short answers - 05
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer{"a_kiss_progress": 6, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_lesson_completed
    - action_restart

## Scenario of utter return_to_previous_question - 01
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 1,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter return_to_previous_question - 02
* nonexclamation__positive__materialpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 2,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter return_to_previous_question - 03
* nonexclamation__positive__materialpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 3,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of utter return_to_previous_question - 04
* nonexclamation__positive__materialpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 4,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of utter return_to_previous_question - 05
* nonexclamation__positive__materialpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 5,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of utter return_to_previous_question - 06
* nonexclamation__positive__materialpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 6,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of utter_can_not_understand - 01
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 1, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter_can_not_understand - 02
* nonexclamation__positive__materialpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 2, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of utter_can_not_understand - 03
* nonexclamation__positive__materialpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 3, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of utter_can_not_understand - 04
* nonexclamation__positive__materialpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 4, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of utter_can_not_understand - 05
* nonexclamation__positive__materialpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 5, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of utter_can_not_understand - 06
* nonexclamation__positive__materialpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 6, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful
