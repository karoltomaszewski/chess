from django import forms

class MainForm(forms.Form):
    username = forms.CharField(label=False)