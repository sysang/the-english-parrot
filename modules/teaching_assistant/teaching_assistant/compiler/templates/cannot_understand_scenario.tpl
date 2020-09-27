
{% if turn.progress != 0 %}
## Scenario of utter [ {{ turn.scenario_case|upper() }} # {{ turn.progress }}]
* nonexclamation__positive__materialpr OR nonexclamation__negative__materialpr OR nonexclamation__negative__identifyingpr OR nonexclamation__positive__attributivepr OR nonexclamation__negative__attributivepr OR nonexclamation__positive__mentalpr OR nonexclamation__negative__mentalpr OR affirmative__nominalgroup OR affirmative__adjectivegroup OR affirmative__shortanswer OR negative__shortanswer
- slot{"a_kiss_progress": {{ turn.progress }}, "nlu_confused": "positive", "nlu_confident": null}
- followup{"name": "utter_can_not_understand"}
- utter_can_not_understand
- action_reset_nlu_confused_slot
- slot{"a_kiss_progress": {{ turn.progress}}, "nlu_confused": null, "nlu_confident": "positive", "will_return": null}
{%- include 'prev_checkpoint.inc' -%}
{%- endif %}
