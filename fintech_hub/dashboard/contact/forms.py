from django import forms

from apps.contact.models.contact import ContactModel


class ContactForm1(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

