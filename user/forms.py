from typing import ClassVar
from django import forms

class MainForm(forms.Form):
    username = forms.CharField(required=True, label='Nickname')