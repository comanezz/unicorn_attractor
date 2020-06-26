from django import forms
from .models import Feature, Comment


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('context',)
        labels = {'context': ''}
        widgets = {'context': forms.Textarea(
            attrs={'placeholder': 'Comment here', 'rows': '3', 'cols': '200'}),
        }
