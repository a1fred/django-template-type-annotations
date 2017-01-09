from django import template

register = template.Library()


def do_var(variable, variable_type_string):
    """
        may be add some logic, but now empty
    """
    return ''


@register.tag(name='vars')
def do_vars(parser, token):
    nodelist = parser.parse(('endvars', ))

    # Validate annotation format. Not sure we really need this.
    # Raise exceptions in templates may be not good idea.
    # Maybe better idea to keep validation process to editors and tools and skip all logic in runtime.
    for node in nodelist:
        annotations = node.s.split('\n')

        for annotation in annotations:
            annotation = annotation.strip()
            if annotation == '':
                continue

            # Split by : and filter empty items
            annotation_args = [str(x).strip() for x in annotation.split(':')]

            if len(annotation_args) != 2:
                raise ValueError("Incorrect type annotation string: '%s'." % annotation)
            if annotation_args[0].strip() == '':
                raise ValueError("Empty variable name in annotation string: '%s'." % annotation)
            if annotation_args[1].strip() == '':
                raise ValueError("Empty type in annotation string: '%s'." % annotation)

            # Maybe call do_var(*annotation_args)

    parser.delete_first_token()
    return template.defaulttags.CommentNode()


register.simple_tag(do_var, name='var')
