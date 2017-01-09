from unittest import TestCase

from django.template import Template, Context


class TemplateTypeAnnotationTests(TestCase):
    def _render_template_string(self, template_string, ctx={}):
        return Template("{% load defaulttags %}" + str(template_string)).render(Context(ctx))

    def test_var(self):
        self.assertEqual(self._render_template_string("{% var request 'django.http.HttpRequest' %}Hello"), 'Hello')

    def test_vars(self):
        self.assertEqual(
            self._render_template_string("""
{% vars %}
request 'django.http.HttpRequest'
object_list 'django.db.models.query.QuerySet'
{% endvars %}
Hello

""").strip(),
            'Hello'
        )

        with self.assertRaises(ValueError):
            self._render_template_string("""
{% vars %}
object_list 'django.db.models.query.QuerySet' asd
'django.db.models.query.QuerySet'
{% endvars %}
Hello
""")
