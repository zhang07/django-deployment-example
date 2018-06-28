from django import learning_templates

register = template.Library()

def cut(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

    register.filer('cut',cut)
