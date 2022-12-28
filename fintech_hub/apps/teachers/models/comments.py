from django.db import models
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'teacher/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


class CommentsModel(models.Model):
    title = models.CharField(max_length=55)
    body = models.TextField()
    author_image = models.ImageField(upload_to=upload_location)
    author_name = models.CharField(max_length=55)
    author_speciality = models.CharField(max_length=55)

    def __str__(self):
        return str(f"{self.title}-{self.author_name}")
