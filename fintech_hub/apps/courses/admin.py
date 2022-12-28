from django.contrib import admin
from apps.courses.models.courses import CourseModel
from apps.courses.models.facts import FactsModel


admin.site.register(CourseModel)
admin.site.register(FactsModel)
