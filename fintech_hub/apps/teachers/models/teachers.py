from django.db import models
from uuid import uuid4
from apps.courses.models.courses import CourseModel

RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'teacher/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


default_lvl_choise = [
     ('Junior', 'Junior'),
     ('Middle', 'Middle'),
     ('Senior', 'Senior'),
 ]


class TeacherModel(models.Model):
    image = models.ImageField(upload_to=upload_location)
    teacher = models.CharField(max_length=255)
    course = models.ForeignKey(CourseModel, related_name='courses', on_delete=models.SET_NULL, null=True)
    about = models.TextField()
    experience = models.CharField(max_length=55)
    social_network1 = models.URLField(max_length=255, null=True, blank=True)
    social_network2 = models.URLField(max_length=255, null=True, blank=True)
    social_network3 = models.URLField(max_length=255, null=True, blank=True)
    social_network4 = models.URLField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True)
    teacher_level = models.CharField(max_length=255, choices=default_lvl_choise)

    def __str__(self):
        return str(f"{self.id}-{self.teacher}-{self.course}")
