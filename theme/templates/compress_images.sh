#!/usr/bin/env bash

{% for article in articles %}
{% if article.photo %}
{% for width in IMAGE_WIDTHS %}
convert images/{{ article.photo }} -resize {{ width }} images/{{ article.photo|replace('.jpg', '') }}-{{ width }}.jpg
convert images/{{ article.photo }} -resize {{ width }} images/{{ article.photo|replace('.jpg', '') }}-{{ width }}.webp
{% endfor %}
{% endif %}
{% endfor %}
