from django import forms
from apps.courses.models.courses import CourseModel


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
