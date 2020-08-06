## Scenario - main discussion path
* client_initializes_a_kiss_story
    - slot{"story_topic" : "a-kiss-story"}
    - utter_introduce_lesson
    - utter_initializes_a_kiss_story
    - utter_a_kiss_question_DidCarlosBuyOldCar
    - slot{"a_kiss_progress" :["DidCarlosBuyOldCar"]}
* nonexclamation__positive__materialpr{"actor": "he", "materialpr": "bought", "goal": "new car"} OR nonexclamation__negative__materialpr{"actor": "he", "materialpr": "buy", "goal": "old car"}
    - utter_a_kiss_question_DidCarlosBuyExpensiveBicycle
    - slot{"a_kiss_progress" :["DidCarlosBuyOldCar", "DidCarlosBuyExpensiveBicycle"]}
* nonexclamation__positive__identifyingpr{"identified": "it","identifier": "car"}
    - utter_a_kiss_question_HowBigWasCar
    - slot{"a_kiss_progress" :["DidCarlosBuyOldCar", "DidCarlosBuyExpensiveBicycle", "HowBigWasCar"]}
