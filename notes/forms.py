from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title (optional)'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your note or mini-article here...', 'rows':6}),
        }

