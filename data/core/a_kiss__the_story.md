## Core thread of scenario
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
    - slot{"lesson_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car", "confused": "positive"} OR affirmative__nominalgroup{"nominalgrp": "a new car", "confused": "positive"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - slot{"lesson_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle", "confused": "positive"} OR affirmative__nominalgroup{"nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - slot{"lesson_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge", "confused": "positive"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - slot{"lesson_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue", "confused": "positive"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - slot{"lesson_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl", "confused": "positive"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - slot{"lesson_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful", "confused": "positive"}
    - utter_lesson_completed

## Branch 02
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car", "confused": "positive"} OR affirmative__nominalgroup{"nominalgrp": "a new car", "confused": "positive"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - slot{"lesson_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 02 - negative__shortanswer{"nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer{}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - slot{"lesson_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 03
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle", "confused": "positive"} OR affirmative__nominalgroup{"nominalgrp": "a car", "confused": "positive"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - slot{"lesson_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 03 - negative__shortanswer{"nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer{"nlu_confused": null, "nlu_confident": "positive", "will_return": null}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - slot{"lesson_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 04
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attributive": "huge"} OR affirmative__adjectivegroup{"adjectivegrp": "huge", "confused": "positive"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - slot{"lesson_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 05
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attributive": "blue"} OR affirmative__nominalgroup{"adjectivegrp": "blue", "confused": "positive"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - slot{"lesson_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 06
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"nominalgrp": "a girl", "confused": "positive"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - slot{"lesson_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 07
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"carrier": "she", "attributive": "beautiful"} OR affirmative__adjectivegroup{"adjectivegrp": "beautiful", "confused": "positive"}
    - utter_lesson_completed

## Branch 07 - affirmative__shortanswer{"nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer{"nlu_confused": null, "nlu_confident": "positive", "will_return": null}
    - utter_lesson_completed

