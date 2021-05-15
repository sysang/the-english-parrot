## Scenario [MAIN] - [00]
* client_initializes_a_kiss_story
    - action_initialize_a_kiss_story
    - slot{"a_kiss_progress": 0, "lesson_topic": "a_kiss_story", "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
    - utter_start_a_kiss_lesson
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "a new car"}
    - slot{"actor": "he", "materialpr": "bought", "goal": "a new car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "a car"}
    - slot{"identified": "it","identifier": "a car"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attribute": "huge"}
    - slot{"carrier": "it","attribute": "huge"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attribute": "blue"}
    - slot{"carrier": "it", "attribute": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"}
    - slot{"senser": "he","mentalpr": "saw", "phenomenon": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"carrier": "she", "attribute": "beautiful"}
    - slot{"carrier": "she", "attribute": "beautiful"}
    - utter_lesson_completed
    - action_restart

## Scenario of [NEGATIVE_FORM] - [01]
> check_a_kiss_01_DidCarlosBuyOldCar
* nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "an old car"}
    - slot{"actor": "he", "materialpr": "buy", "goal": "an old car"}
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of [NEGATIVE_FORM] - [02]
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* nonexclamation__negative__identifyingpr{"identified": "it", "identifier": "a bicycle"}
    - slot{"identified": "it", "identifier": "a bicycle"}
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar

## Scenario of [SHORT_ANSWER] - [01]
> check_a_kiss_01_DidCarlosBuyOldCar
* negative__shortanswer
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of [SHORT_ANSWER] - [02]
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* negative__shortanswer
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar

## Scenario of [SHORT_ANSWER] - [03]
> check_a_kiss_03_HowBigWasCar
* affirmative__adjectivegroup{"adjectivegrp": "huge"}
    - slot{"adjectivegrp": "huge"}
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar

## Scenario of [SHORT_ANSWER] - [04]
> check_a_kiss_04_WhatColorWasCar
* affirmative__adjectivegroup{"adjectivegrp": "blue"}
    - slot{"adjectivegrp": "blue"}
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [SHORT_ANSWER] - [05]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* affirmative__nominalgroup{"nominalgrp": "a girl"}
    - slot{"nominalgrp": "a girl"}
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [SHORT_ANSWER] - [06]
> check_a_kiss_06_DidSheLookBeautiful
* affirmative__shortanswer
    - utter_lesson_completed
    - action_restart

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [01]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 1,"will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [02]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 2,"will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [03]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 3,"will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [04]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 4,"will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [05]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 5,"will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of utter [RETURN_TO_PREVIOUS_QUESTION] - [06]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 6,"will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of utter [CAN_NOT_UNDERSTAND] - [01]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 1, "nlu_confused": "positive", "nlu_confident": null}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_01_DidCarlosBuyOldCar

## Scenario of utter [CAN_NOT_UNDERSTAND] - [02]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 2, "nlu_confused": "positive", "nlu_confident": null}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of utter [CAN_NOT_UNDERSTAND] - [03]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 3, "nlu_confused": "positive", "nlu_confident": null}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar

## Scenario of utter [CAN_NOT_UNDERSTAND] - [04]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 4, "nlu_confused": "positive", "nlu_confident": null}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar

## Scenario of utter [CAN_NOT_UNDERSTAND] - [05]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 5, "nlu_confused": "positive", "nlu_confident": null}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of utter [CAN_NOT_UNDERSTAND] - [06]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
    - slot{"a_kiss_progress": 6, "nlu_confused": "positive", "nlu_confident": null}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
    - action_reset_nlu_confused_slot
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [01]
> check_a_kiss_01_DidCarlosBuyOldCar
* affirmative__shortanswer
    - utter_a_kiss_01_disagree
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle

## Scenario of [WRONG_ANSWER] - [02]
> check_a_kiss_02_DidCarlosBuyExpensiveBicycle
* affirmative__shortanswer
    - utter_a_kiss_02_disagree
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_03_HowBigWasCar

## Scenario of [WRONG_ANSWER] - [03] - [01]
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attribute": "small"}
    - slot{"carrier": "it","attribute": "small"}
    - utter_a_kiss_03_disagree
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar

## Scenario of [WRONG_ANSWER] - [03] - [02]
> check_a_kiss_03_HowBigWasCar
* nonexclamation__positive__attributivepr{"carrier": "it","attribute": "modern"}
    - slot{"carrier": "it","attribute": "modern"}
    - utter_a_kiss_03_disagree
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_04_WhatColorWasCar

## Scenario of [WRONG_ANSWER] - [04] - [01]
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attribute": "green"}
    - slot{"carrier": "it", "attribute": "green"}
    - utter_a_kiss_04_disagree
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [WRONG_ANSWER] - [04] - [02]
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attribute": "brown"}
    - slot{"carrier": "it", "attribute": "brown"}
    - utter_a_kiss_04_disagree
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [WRONG_ANSWER] - [04] - [03]
> check_a_kiss_04_WhatColorWasCar
* nonexclamation__positive__attributivepr{"carrier": "it", "attribute": "bright"}
    - slot{"carrier": "it", "attribute": "bright"}
    - utter_a_kiss_04_disagree
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee

## Scenario of [WRONG_ANSWER] - [05] - [01]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "a boy"}
    - slot{"senser": "he","mentalpr": "saw", "phenomenon": "a boy"}
    - utter_a_kiss_05_disagree
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [05] - [02]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* nonexclamation__positive__mentalpr{"senser": "he","mentalpr": "saw", "phenomenon": "an egg"}
    - slot{"senser": "he","mentalpr": "saw", "phenomenon": "an egg"}
    - utter_a_kiss_05_disagree
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [05] - [03]
> check_a_kiss_05_WhileDrivingDownWhatDidHeSee
* affirmative__nominalgroup{"nominalgrp": "men"}
    - slot{"nominalgrp": "men"}
    - utter_a_kiss_05_disagree
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history__a_kiss
    - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
> check_a_kiss_06_DidSheLookBeautiful

## Scenario of [WRONG_ANSWER] - [06] - [01]
> check_a_kiss_06_DidSheLookBeautiful
* negative__shortanswer
    - utter_a_kiss_06_disagree
    - utter_lesson_completed
    - action_restart

## Scenario of [WRONG_ANSWER] - [06] - [02]
> check_a_kiss_06_DidSheLookBeautiful
* nonexclamation__positive__attributivepr{"carrier": "she", "attribute": "ugly"}
    - slot{"carrier": "she", "attribute": "ugly"}
    - utter_a_kiss_06_disagree
    - utter_lesson_completed
    - action_restart
