
## interactive_story_1
* client_initializes_a_kiss_story
    - utter_start_a_kiss_lesson
    - action_initialize_a_kiss_story
    - slot{"lesson_topic": "a_kiss_story"}
    - utter_a_kiss_01_DidCarlosBuyOldCar
    - action_store_lesson_history
    - slot{"will_return": null}
    - slot{"confused": null}
    - slot{"lesson_history": [1]}
    - slot{"lesson_progress": 1}
* nonexclamation__negative__attributivepr
    - action_not_understand_fallback
    - slot{"confused": "positive"}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
* nonexclamation__negative__attributivepr
    - action_not_understand_fallback
    - slot{"confused": "positive"}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
* nonexclamation__negative__attributivepr
    - action_not_understand_fallback
    - slot{"confused": "positive"}
    - followup{"name": "utter_can_not_understand"}
    - utter_can_not_understand
* negative__shortanswer
    - action_not_sure_what_to_do_fallback
    - slot{"will_return": "positive"}
* negative__shortanswer
    - utter_return_to_previous_question
