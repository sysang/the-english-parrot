## utter_can_not_understand then listen
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 1, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - followup{"name": "utter_can_not_understand"}
    - action_listen

## Return to question when not sure what to do next
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 1, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"lesson_progress": 1, "nlu_confused": "positive", "nlu_confident": null, "will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history

## Return to question when not sure what to do next
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 2, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"lesson_progress": 2, "nlu_confused": "positive", "nlu_confident": null, "will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_02_DidCarlosBuyExpensiveBicycle
    - action_store_lesson_history

## Return to question when not sure what to do next
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 1, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"lesson_progress": 3, "nlu_confused": "positive", "nlu_confident": null, "will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_03_HowBigWasCar
    - action_store_lesson_history

## Return to question when not sure what to do next
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 4, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"lesson_progress": 4, "nlu_confused": "positive", "nlu_confident": null, "will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_04_WhatColorWasCar
    - action_store_lesson_history

## Return to question when not sure what to do next
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 5, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"lesson_progress": 5, "nlu_confused": "positive", "nlu_confident": null, "will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_05_WhileDrivingDownWhatDidHeSee
    - action_store_lesson_history

## Return to question when not sure what to do next
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup{"lesson_progress": 6, "conconfused": "positive"} OR affirmative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null} OR negative__shortanswer{"nlu_confused": "positive", "nlu_confident": null, "will_return": null}
    - slot{"lesson_progress": 6, "nlu_confused": "positive", "nlu_confident": null, "will_return": "positive"}
    - followup{"name": "utter_return_to_previous_question"}
    - utter_return_to_previous_question
    - utter_a_kiss_06_DidSheLookBeautiful
    - action_store_lesson_history
