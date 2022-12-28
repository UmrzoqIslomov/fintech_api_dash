from django import forms
from apps.teachers.models.comments import CommentsModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = '__all__'



