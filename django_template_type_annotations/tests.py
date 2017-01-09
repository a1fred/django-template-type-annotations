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
request: django.http.HttpRequest
object_list: django.db.models.query.QuerySet
{% endvars %}
Hello

""").strip(),
            'Hello'
        )

        with self.assertRaisesRegex(ValueError, r'Incorrect type annotation string: .*'):
            self._render_template_string("""
                {% vars %}
                :'django.db.models.query.QuerySet':
                {% endvars %}
                Hello
            """)

        with self.assertRaisesRegex(ValueError, r'Empty variable name in annotation string: .*'):
            self._render_template_string("""
                {% vars %}
                :'django.db.models.query.QuerySet'
                {% endvars %}
                Hello
            """)

        with self.assertRaisesRegex(ValueError, r'Empty type in annotation string: .*'):
            self._render_template_string("""
                {% vars %}
                'django.db.models.query.QuerySet':
                {% endvars %}
                Hello
            """)
