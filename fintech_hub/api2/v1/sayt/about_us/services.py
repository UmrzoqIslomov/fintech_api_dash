from collections import OrderedDict

from apps.about_us.models.about_us import AboutUsModel
from base.sqlpaginator import SqlPaginator
from django_app.settings import PER_PAGE


def about_pag(requests):
    about = AboutUsModel.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset + limit):
        try:
            result.append(about_format(about[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(about))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_about(data):
    return OrderedDict([
        ("items", about_format(data)),
    ])


def about_format(data):
    return OrderedDict([
        ('id', data.id),
        ('title', data.title),
        ('body', data.body),
        ('image1', data.image1.url),
        ('image2', data.image2.url),
        ('fact1', data.fact1),
        ('fact2', data.fact2),
    ])
