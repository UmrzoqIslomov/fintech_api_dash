from django.db import models
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'courses/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


class FactsModel(models.Model):
    image = models.ImageField(upload_to=upload_location)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    graduates = models.CharField(max_length=55)
    employment = models.CharField(max_length=55)
    salary = models.CharField(max_length=55)
    video = models.FileField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(f"{self.id}-{self.title}")




