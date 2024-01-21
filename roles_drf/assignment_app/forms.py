# forms.py
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Answer, Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date']
        widgets = {
            'description': SummernoteWidget(),
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }

class AnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        read_only = kwargs.pop('read_only', False)
        super(AnswerForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = read_only
            field.widget.attrs['readOnly'] = read_only

    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': SummernoteWidget(),
        }
