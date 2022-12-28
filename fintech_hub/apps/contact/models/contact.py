from django.db import models


class ContactModel(models.Model):
    location = models.CharField(max_length=255)
    social_network1 = models.URLField(max_length=255, blank=True, null=True)
    social_network2 = models.URLField(max_length=255, blank=True, null=True)
    social_network3 = models.URLField(max_length=255, blank=True, null=True)
    social_network4 = models.URLField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=155)

    def __str__(self):
        return str(self.location)

