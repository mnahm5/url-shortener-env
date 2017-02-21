from django import forms

from .validators import validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='URL', validators={validate_url})