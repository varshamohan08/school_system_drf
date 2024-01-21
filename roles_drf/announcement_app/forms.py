# forms.py
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'expiration_date']
        widgets = {
            'content': SummernoteWidget(),
            'expiration_date': forms.TextInput(attrs={'type': 'date'}),
        }
