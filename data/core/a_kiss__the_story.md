## Core thread of scenario
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "nlu_confident": "positive", "actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "nlu_confident": "positive", "actor": "he", "materialpr": "buy", "goal": "an old car", "confused": "positive"} OR affirmative__nominalgroup{"a_kiss_progress": 1, "nlu_confident": "positive", "nominalgrp": "a new car", "confused": "positive"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"a_kiss_progress": 2, "nlu_confident": "positive", "identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "nlu_confident": "positive", "identified": "it", "identifier": "a bicycle", "confused": "positive"} OR affirmative__nominalgroup{"a_kiss_progress": 2, "nlu_confident": "positive", "nominalgrp": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confident": "positive", "carrier": "it","attribute": "huge"} OR affirmative__adjectivegroup{"a_kiss_progress": 3, "nlu_confident": "positive", "adjectivegrp": "huge", "confused": "positive"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confident": "positive", "carrier": "it", "attribute": "blue"} OR affirmative__nominalgroup{"a_kiss_progress": 4, "nlu_confident": "positive", "adjectivegrp": "blue", "confused": "positive"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confident": "positive", "senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"a_kiss_progress": 5, "nlu_confident": "positive", "nominalgrp": "a girl", "confused": "positive"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "nlu_confident": "positive", "carrier": "she", "attribute": "beautiful"} OR affirmative__adjectivegroup{"a_kiss_progress": 6, "nlu_confident": "positive", "adjectivegrp": "beautiful", "confused": "positive"}
    - utter_lesson_completed
    - action_restart

## Branch 02
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"a_kiss_progress": 1, "nlu_confident": "positive", "actor": "he", "materialpr": "bought", "goal": "a new car"} OR nonexclamation__negative__materialpr{"a_kiss_progress": 1, "nlu_confident": "positive", "actor": "he", "materialpr": "buy", "goal": "an old car", "confused": "positive"} OR affirmative__nominalgroup{"nominalgrp": "a new car", "confused": "positive"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 02 - negative__shortanswer
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer{"a_kiss_progress": 1, "nlu_confident": "positive"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 03
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"a_kiss_progress": 2, "nlu_confident": "positive", "identified": "it","identifier": "a car"} OR nonexclamation__negative__identifyingpr{"a_kiss_progress": 2, "nlu_confident": "positive", "identified": "it", "identifier": "a bicycle", "confused": "positive"} OR affirmative__nominalgroup{"a_kiss_progress": 2, "nlu_confident": "positive", "nominalgrp": "a car", "nlu_confident": "positive", "confused": "positive"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 03 - negative__shortanswer
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer{"a_kiss_progress": 2, "nlu_confident": "positive"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 04
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 3, "nlu_confident": "positive", "carrier": "it","attribute": "huge"} OR affirmative__adjectivegroup{"a_kiss_progress": 3, "nlu_confident": "positive", "adjectivegrp": "huge", "confused": "positive"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 05
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"a_kiss_progress": 4, "nlu_confident": "positive", "carrier": "it", "attribute": "blue"} OR affirmative__nominalgroup{"a_kiss_progress": 4, "nlu_confident": "positive", "adjectivegrp": "blue", "confused": "positive"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 06
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"a_kiss_progress": 5, "nlu_confident": "positive", "senser": "he","mentalpr": "saw", "phenomenon": "a girl"} OR affirmative__nominalgroup{"a_kiss_progress": 5, "nlu_confident": "positive", "nominalgrp": "a girl", "confused": "positive"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}

## Branch 07
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"a_kiss_progress": 6, "nlu_confident": "positive", "carrier": "she", "attribute": "beautiful"} OR affirmative__adjectivegroup{"a_kiss_progress": 6, "nlu_confident": "positive", "adjectivegrp": "beautiful", "confused": "positive"}
    - utter_lesson_completed
    - action_restart

## Branch 07 - affirmative__shortanswer{"nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer{"a_kiss_progress": 6, "nlu_confident": "positive"}
    - utter_lesson_completed
    - action_restart

