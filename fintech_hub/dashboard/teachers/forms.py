from django import forms

from apps.teachers.models.teachers import TeacherModel


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = '__all__'

