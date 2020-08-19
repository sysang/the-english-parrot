## Core thread of scenario
* client_initializes_changed_story
  - action_initialize_changed_story
  - slot{"changed_progress": 0, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_start_a_changed_lesson
  - utter_changed_01_WhereDidSheLive
  - action_store_lesson_history__changed
  - slot{"changed_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
> check_changed_01_WhereDidSheLive
* nonexclamation__positive__materialpr{"changed_progress": 1, "nlu_confident": "positive", "actor": "she", "materialpr": "lived", "scope": "in phoenix", "lesson_topic": "changed_story"} OR affirmative__prepositionalphrase__location{"changed_progress": 1, "nlu_confident": "positive", "prepositionallocation": "in phoenix", "lesson_topic": "changed_story"}
  - utter_changed_02_DidGracHaveProblem
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
> check_changed_02_DidGracHaveProblem
* nonexclamation__positive__attributivepr{"changed_progress": 2, "nlu_confident": "positive", "carrier": "she", "attributivepr": "had", "attribute": "a problem", "lesson_topic": "changed_story"} OR affirmative__shortanswer{"changed_progress": 2, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_03_DidSheHaveProblemHerChildren
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
> check_changed_03_DidSheHaveProblemHerChildren
* nonexclamation__negative__attributivepr{"changed_progress": 3, "nlu_confident": "positive", "carrier": "she", "attributivepr": "have", "attribute": "a problem with her children", "lesson_topic": "changed_story"} OR negative__shortanswer{"changed_progress": 3, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_04_DidSheHaveProblemHerMom
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
> check_changed_04_DidSheHaveProblemHerMom
* nonexclamation__negative__attributivepr{"changed_progress": 4, "nlu_confident": "positive", "carrier": "she", "attributivepr": "have", "attribute": "a problem with her mom", "lesson_topic": "changed_story"} OR negative__shortanswer{"changed_progress": 4, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_05_DidSheHaveProblemHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
> check_changed_05_DidSheHaveProblemHerHusband
* nonexclamation__positive__attributivepr{"changed_progress": 5, "nlu_confident": "positive", "carrier": "she", "attributivepr": "have", "attribute": "a problem with her husband", "lesson_topic": "changed_story"} OR affirmative__shortanswer{"changed_progress": 5, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_06_WhichProblemDidSheHaveHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
> check_changed_06_WhichProblemDidSheHaveHerHusband
* nonexclamation__negative__materialpr{"changed_progress": 6, "nlu_confident": "positive", "actor": "he", "materialpr": "show", "goal": "any affection", "lesson_topic": "changed_story", "lesson_topic": "changed_story"} OR affirmative__prepositionalphrase__location{"changed_progress": 6, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_lesson_completed
  - action_restart

## scenario of short answers
* client_initializes_changed_story
  - action_initialize_changed_story
  - slot{"lesson_topic": "changed_story"}
  - utter_start_a_changed_lesson
  - utter_changed_01_WhereDidSheLive
  - action_store_lesson_history__changed
  - slot{"changed_progress": 1, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
* affirmative__prepositionalphrase__location{"changed_progress": 1, "nlu_confident": "positive", "prepositionallocation": "in phoenix", "lesson_topic": "changed_story"}
  - utter_changed_02_DidGracHaveProblem
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
* affirmative__shortanswer{"changed_progress": 2, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_03_DidSheHaveProblemHerChildren
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
* negative__shortanswer{"changed_progress": 3, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_04_DidSheHaveProblemHerMom
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
* negative__shortanswer{"changed_progress": 4, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_05_DidSheHaveProblemHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
* affirmative__shortanswer{"changed_progress": 5, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_06_WhichProblemDidSheHaveHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}
* affirmative__nominalgroup{"changed_progress": 6, "nlu_confident": "positive", "nominalgrp": "no affection", "lesson_topic": "changed_story"}
  - utter_lesson_completed
  - action_restart

## Branch 01
> check_changed_01_WhereDidSheLive
* nonexclamation__positive__materialpr{"changed_progress": 1, "nlu_confident": "positive", "actor": "she", "materialpr": "lived", "scope": "in phoenix", "lesson_topic": "changed_story"}
  - utter_changed_02_DidGracHaveProblem
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 01 - affirmative__prepositionalphrase__location
> check_changed_01_WhereDidSheLive
* affirmative__prepositionalphrase__location{"changed_progress": 1, "nlu_confident": "positive", "prepositionallocation": "in phoenix", "lesson_topic": "changed_story"}
  - utter_changed_02_DidGracHaveProblem
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 2, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 02
> check_changed_02_DidGracHaveProblem
* nonexclamation__positive__attributivepr{"changed_progress": 2, "nlu_confident": "positive", "carrier": "she", "attributivepr": "had", "attribute": "a problem", "lesson_topic": "changed_story"}
  - utter_changed_03_DidSheHaveProblemHerChildren
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 02 - affirmative__shortanswer
> check_changed_02_DidGracHaveProblem
* affirmative__shortanswer{"changed_progress": 2, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_03_DidSheHaveProblemHerChildren
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 3, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 03
> check_changed_03_DidSheHaveProblemHerChildren
* nonexclamation__negative__attributivepr{"changed_progress": 3, "nlu_confident": "positive", "carrier": "she", "attributivepr": "have", "attribute": "a problem with her children", "lesson_topic": "changed_story"}
  - utter_changed_04_DidSheHaveProblemHerMom
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 03 - negative__shortanswer
> check_changed_03_DidSheHaveProblemHerChildren
* negative__shortanswer{"changed_progress": 3, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_04_DidSheHaveProblemHerMom
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 4, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 04
> check_changed_04_DidSheHaveProblemHerMom
* nonexclamation__negative__attributivepr{"changed_progress": 4, "nlu_confident": "positive", "carrier": "she", "attributivepr": "have", "attribute": "a problem with her mom", "lesson_topic": "changed_story"}
  - utter_changed_05_DidSheHaveProblemHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 04 - negative__shortanswer
> check_changed_04_DidSheHaveProblemHerMom
* negative__shortanswer{"changed_progress": 4, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_05_DidSheHaveProblemHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 5, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 05
> check_changed_05_DidSheHaveProblemHerHusband
* nonexclamation__positive__attributivepr{"changed_progress": 5, "nlu_confident": "positive", "carrier": "she", "attributivepr": "have", "attribute": "a problem with her husband", "lesson_topic": "changed_story"}
  - utter_changed_06_WhichProblemDidSheHaveHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 05 - affirmative__shortanswer
> check_changed_05_DidSheHaveProblemHerHusband
* affirmative__shortanswer{"changed_progress": 5, "nlu_confident": "positive", "lesson_topic": "changed_story"}
  - utter_changed_06_WhichProblemDidSheHaveHerHusband
  - action_store_lesson_history__changed
  - slot{"a_kiss_progress": 6, "nlu_confused": null, "nlu_confident": "positive", "will_return": null, "lesson_topic": "changed_story"}

## Branch 06
> check_changed_06_WhichProblemDidSheHaveHerHusband
* nonexclamation__negative__materialpr{"changed_progress": 6, "nlu_confident": "positive", "actor": "he", "materialpr": "show", "goal": "any affection", "lesson_topic": "changed_story"}
  - utter_lesson_completed
  - action_restart

## Branch 06 - affirmative__nominalgroup
> check_changed_06_WhichProblemDidSheHaveHerHusband
* affirmative__nominalgroup{"changed_progress": 6, "nlu_confident": "positive", "nominalgrp": "no affection", "lesson_topic": "changed_story"}
  - utter_lesson_completed
  - action_restart
