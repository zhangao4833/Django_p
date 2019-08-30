from django.template.defaultfilters import register
import os
@register.filter('ellipse')
def ellipse(value):
    return os.path.splitext(value)[-1]