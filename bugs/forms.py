from django import forms
from .models import Bug, Comment


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('context',)
        labels = {'context': ''}
        widgets = {'context': forms.Textarea(
            attrs={'placeholder': 'Comment here', 'rows': '3', 'cols': '200'}),
        }
