from django import forms
from apps.courses.models.facts import FactsModel


class FactForm(forms.ModelForm):
    class Meta:
        model = FactsModel
        fields = '__all__'
