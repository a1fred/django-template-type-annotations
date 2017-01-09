from django import template

register = template.Library()


def do_var(variable, variable_type_string):
    """
        may be add some logic, but now empty
    """
    return ''


@register.tag(name='vars')
def do_vars(parser, token):
    nodelist = parser.parse(('endvars',))

    # Validate annotation format
    for node in nodelist:
        annotations = filter(None, node.s.split('\n'))
        for annotation in annotations:
            annotation = annotation.strip()
            annotation_args = annotation.split()
            if len(annotation_args) != 2:
                raise ValueError("Incorrect type annotation string: '%s'." % annotation)
            else:
                pass
                # Maybe call do_var(*annotation_args)

    parser.delete_first_token()
    return template.defaulttags.CommentNode()


register.simple_tag(do_var, name='var')
