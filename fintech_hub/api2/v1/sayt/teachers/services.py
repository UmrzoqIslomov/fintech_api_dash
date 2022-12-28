from collections import OrderedDict

from api2.v1.sayt.courses.services import courses_format
from apps.teachers.models.teachers import TeacherModel
from base.sqlpaginator import SqlPaginator
from django_app.settings import PER_PAGE


def teachers_pag(requests):
    partners = TeacherModel.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset + limit):
        try:
            result.append(teachers_format(partners[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(partners))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_teachers(data):
    return OrderedDict([
        ("items", teachers_format(data)),
    ])


def teachers_format(data):
    return OrderedDict([
        ('id', data.id),
        ('image', data.image.url),
        ('teacher', data.teacher),
        ('course', courses_format(data.course) if data.course else None),
        ('about', data.about),
        ('experience', data.experience),
        ('social_network1', data.social_network1),
        ('social_network2', data.social_network2),
        ('social_network3', data.social_network3),
        ('social_network4', data.social_network4),
        ('rating', data.rating),
        ('teacher_level', data.teacher_level),
    ])
