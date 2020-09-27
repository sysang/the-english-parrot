{%- if turn.progress != 0 and not turn.is_last -%}
* {{ turn.intention }}{{ (turn.entities|default('', True)) }}
{%- if turn.entities %}
- slot{{ turn.entities }}
{%- endif %}
- utter_{{ turn.topic }}_{{ turn.progress + 1 }}_{{ turn.going_next }}
- action_store_lesson_history__{{ turn.topic }}
- slot{{ turn.action_slots }}
{%- elif turn.progress == 0 -%}
## Scenario [ {{ turn.scenario_case|upper() }} ]
* client_initialize_{{ turn.topic }}_story
- slot{{ turn.initial_slots }}
- utter_start_{{ turn.topic }}_lesson
- utter_{{ turn.topic }}_{{ turn.progress + 1 }}_{{turn.going_next}}
- action_store_lesson_history__{{ turn.topic }}
- slot{{ turn.action_slots }}
{%- else -%}
* {{ turn.intention }}{{ turn.entities|default('', True)  }}
{%- if turn.entities %}
- slot{{ turn.entities }}
{%- endif %}
- utter_lesson_completed
- action_restart
{%- endif -%}
