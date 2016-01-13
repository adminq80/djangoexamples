from django import forms

class TestForm(forms.Form):
    post = forms.CharField(label='Type something')