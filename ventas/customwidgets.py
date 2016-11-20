__author__ = 'pmmr'

from django.forms import  Select
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from itertools import chain


class ReadOnlySelect(Select):
    """
    This should replace the Select widget with a disabled text widget displaying the value,
    and hidden field with the actual id
    """
    def render(self, name, value, attrs=None, choices=()):
        final_attrs = self.build_attrs(attrs, name=name)
        display = "None"
        for option_value, option_label in chain(self.choices, choices):
            if str(option_value) == (value) :
                display = option_label
        output = format_html('<input type=text value="%s" disabled="disabled" ><input type="hidden" value="%s"  %s> ' % (display, value, flatatt(final_attrs)))

        return mark_safe(output)