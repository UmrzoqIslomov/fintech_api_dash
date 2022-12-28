from django import forms
from apps.partners.models.partners import PartnersModel


class PartnerForm(forms.ModelForm):
    class Meta:
        model = PartnersModel
        fields = '__all__'
