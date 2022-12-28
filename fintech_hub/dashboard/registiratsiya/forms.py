from django import forms
from apps.partners.models.registration import RegistrationModel


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields = '__all__'
