
{% if turn.progress != 0 %}
## Scenario of utter [ {{ turn.scenario_case|upper() }} # {{ turn.progress }}]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
- slot{"a_kiss_progress": {{ turn.progress }},"will_return": "positive"}
- followup{"name": "utter_return_to_previous_question"}
- utter_return_to_previous_question
- utter_{{ turn.topic }}_{{ turn.progress }}_{{ turn.question }}
- action_store_lesson_history__{{ turn.topic }}
- slot{"a_kiss_progress": {{ turn.progress }}, "nlu_confused": null, "will_return": null}
{%- include 'prev_checkpoint.inc' -%}
{%- endif %}
