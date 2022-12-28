from django.contrib import admin
from apps.teachers.models.teachers import TeacherModel
from apps.teachers.models.comments import CommentsModel

admin.site.register(TeacherModel)
admin.site.register(CommentsModel)
