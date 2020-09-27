{%- if turn.going_next %}
> check_{{ turn.topic }}_{{ turn.progress + 1 }}_{{ turn.going_next }}
{% else %}
{% endif %}
