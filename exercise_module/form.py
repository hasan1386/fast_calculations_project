from django import forms
from .models import Exercises
from django.forms.widgets import TextInput


class LTRTextInput(TextInput):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['dir'] = 'ltr'
        super().__init__(attrs=attrs)


class LessonsModelForm(forms.ModelForm):
    title = forms.TextInput()
    operator_type = forms.TextInput()
    calculations = forms.CharField(widget=LTRTextInput, label='سؤال')
    result = forms.IntegerField(widget=LTRTextInput, label='جواب')

    class Meta:
        model = Exercises
        fields = '__all__'