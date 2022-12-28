from django.db import models
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'about_us/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


class AboutUsModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image1 = models.ImageField(upload_to=upload_location)
    image2 = models.ImageField(upload_to=upload_location)
    fact1 = models.TextField(blank=True, null=True)
    fact2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(f"{self.id}-{self.title}")

