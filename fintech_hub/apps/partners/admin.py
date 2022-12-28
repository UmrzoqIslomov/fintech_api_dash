from django.contrib import admin
from apps.partners.models.partners import PartnersModel
from apps.partners.models.registration import RegistrationModel


admin.site.register(PartnersModel)
admin.site.register(RegistrationModel)