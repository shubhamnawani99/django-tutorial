from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        labels = {
            'text': 'Tweet',
            'photo': 'Photo (optional)'
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }