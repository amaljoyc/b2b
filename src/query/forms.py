from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from . import models


class QueryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('category'),
            Field('subject'),
            Field('content'),
            Submit('ask', 'Ask', css_class="btn-success"),
            )

    class Meta:
        model = models.Query
        category = forms.ModelChoiceField(queryset=models.Category.objects.all(), to_field_name="name")
        fields = ['category', 'subject', 'content']
