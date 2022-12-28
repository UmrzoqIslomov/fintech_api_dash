from django.db import models
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'partners/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


class RegistrationModel(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    text = models.TextField()

    def __str__(self):
        return str(self.full_name)
    