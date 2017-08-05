from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from . import models


class OfferForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('content'),
            Submit('offer', 'Offer', css_class="btn-success"),
            )

    class Meta:
        model = models.Offer
        fields = ['content']
