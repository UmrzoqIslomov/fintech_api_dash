from collections import OrderedDict

from apps.partners.models.partners import PartnersModel
from base.sqlpaginator import SqlPaginator
from django_app.settings import PER_PAGE


def partners_pag(requests):
    partners = PartnersModel.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset + limit):
        try:
            result.append(partners_format(partners[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(partners))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_partners(data):
    return OrderedDict([
        ("items", partners_format(data)),
    ])


def partners_format(data):
    return OrderedDict([
        ('id', data.id),
        ('image', data.image.url if data.image else None)
    ])
