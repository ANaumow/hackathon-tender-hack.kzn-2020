from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={"class": "textarea"}), label='')
