# Django template type annotations tags
[![Build Status](https://travis-ci.org/a1fred/django-template-type-annotations.svg?branch=master)](https://travis-ci.org/a1fred/django-template-type-annotations)
[![Coverage Status](https://coveralls.io/repos/github/a1fred/django-template-type-annotations/badge.svg?branch=master)](https://coveralls.io/github/a1fred/django-template-type-annotations?branch=master)


# Usage
I created two tags for one-line and multiline annotation.

```
{% var request 'django.http.HttpRequest' %}

or

{% vars %}
request 'django.http.HttpRequest'
object_list 'django.db.models.query.QuerySet'
{% endvars %}
```
