from django import forms
from apps.about_us.models.about_us import AboutUsModel


class AboutUsForms(forms.ModelForm):
    class Meta:
        model = AboutUsModel
        fields = '__all__'
