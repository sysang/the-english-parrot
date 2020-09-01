## Scenario [MAIN] - [00]
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

## Scenario of [SHORT_ANSWER] - [01]
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer{"a_kiss_progress": 1, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of [SHORT_ANSWER] - [02]
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer{"a_kiss_progress": 2, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of [SHORT_ANSWER] - [03]
> check_a_kiss_03_HowBigWasCar
* affirmative__adjectivegroup{"a_kiss_progress": 3, "nlu_confident": "positive", "adjectivegrp": "huge", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of [SHORT_ANSWER] - [04]
> check_a_kiss_04_WhatColorWasCar
* affirmative__adjectivegroup{"a_kiss_progress": 4, "nlu_confident": "positive", "adjectivegrp": "blue", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [SHORT_ANSWER] - [05]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* affirmative__nominalgroup{"a_kiss_progress": 5, "nlu_confident": "positive", "nominalgrp": "a girl", "confused": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [SHORT_ANSWER] - [06]
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer{"a_kiss_progress": 6, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_lesson_completed
    - action_restart

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [01]
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 1, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 1,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [02]
* nonexclamation__positive__materialpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 2, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 2,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [03]
* nonexclamation__positive__materialpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 3, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 3,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [04]
* nonexclamation__positive__materialpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 4, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 4,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [05]
* nonexclamation__positive__materialpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 5, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 5,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [06]
* nonexclamation__positive__materialpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 6, "will_return": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 6,"will_return": "positive", "lesson_topic": "a_kiss_story"}
    - utter_return_to_previous_question
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of utter [CAN_NOT_UNDERSTAND] - [01]
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 1, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 1, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter [CAN_NOT_UNDERSTAND] - [02]
* nonexclamation__positive__materialpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 2, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 2, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of utter [CAN_NOT_UNDERSTAND] - [03]
* nonexclamation__positive__materialpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 3, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 3, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of utter [CAN_NOT_UNDERSTAND] - [04]
* nonexclamation__positive__materialpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 4, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 4, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of utter [CAN_NOT_UNDERSTAND] - [05]
* nonexclamation__positive__materialpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 5, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 5, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of utter [CAN_NOT_UNDERSTAND] - [06]
* nonexclamation__positive__materialpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__attributivepr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__positive__mentalpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR nonexclamation__negative__mentalpr{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__nominalgroup{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__adjectivegroup{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR affirmative__shortanswer{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"} OR negative__shortanswer{"a_kiss_progress": 6, "nlu_confused": "positive", "lesson_topic": "a_kiss_story"}
    - slot{"a_kiss_progress": 6, "nlu_confused": "positive", "nlu_confident": null, "will_return": null, "lesson_topic": "a_kiss_story"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [01]
> check_a_kiss_01_DidCarlosBuyOldCar
* affirmative__shortanswer{"a_kiss_progress": 1, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_disagree
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of [WRONG_ANSWER] - [02]
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* affirmative__shortanswer{"a_kiss_progress": 2, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_02_disagree
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_03_HowBigWasCar

## Scenario of [WRONG_ANSWER] - [03] - [01]
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confident": "positive", "carrier": "it","attribute": "small", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_03_disagree
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar

## Scenario of [WRONG_ANSWER] - [03] - [02]
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confident": "positive", "carrier": "it","attribute": "any", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_03_disagree
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_04_WhatColorWasCar
## Scenario of [WRONG_ANSWER] - [04] - [01]

> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confident": "positive", "carrier": "it", "attribute": "green", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_04_disagree
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [WRONG_ANSWER] - [04] - [02]
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confident": "positive", "carrier": "it", "attribute": "dark", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_04_disagree
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [WRONG_ANSWER] - [04] - [03]
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confident": "positive", "carrier": "it", "attribute": "any", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_04_disagree
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [WRONG_ANSWER] - [05] - [01]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confident": "positive", "senser": "he","mentalpr": "saw", "phenomenon": "a boy", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_05_disagree
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [05] - [02]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confident": "positive", "senser": "he","mentalpr": "saw", "phenomenon": "any", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_05_disagree
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "a_kiss_story"}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [06] - [01]
> check_a_kiss_06_DidSheLookBeautiful
* negative__shortanswer{"a_kiss_progress": 6, "nlu_confident": "positive", "lesson_topic": "a_kiss_story"}
    - utter_a_kiss_06_disagree
    - utter_lesson_completed
    - action_restart
