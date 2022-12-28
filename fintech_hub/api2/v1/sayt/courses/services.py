from collections import OrderedDict

from apps.courses.models.courses import CourseModel
from base.sqlpaginator import SqlPaginator
from django_app.settings import PER_PAGE


def courses_pag(requests):
    courses = CourseModel.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset + limit):
        try:
            result.append(courses_format(courses[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(courses))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_courses(data):
    return OrderedDict([
        ("items", courses_format(data)),
    ])


def courses_format(data):
    return OrderedDict([
        ('id', data.id),
        ('image', data.image.url),
        ('teacher', data.teacher),
        ('course', data.course),
        ('price', data.price),
        ('lessons_amount', data.lessons_amount),
        ('lesson_duration', data.lesson_duration),
    ])
