from collections import OrderedDict

from apps.contact.models.contact import ContactModel
from base.sqlpaginator import SqlPaginator
from django_app.settings import PER_PAGE


def contact_pag(requests):
    contact = ContactModel.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page-1) * limit

    result = []
    for i in range(offset, offset + limit):
        try:
            result.append(contact_format(contact[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(contact))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_contact(data):
    return OrderedDict([
        ("items", contact_format(data)),
    ])


def contact_format(data):
    return OrderedDict([
        ('id', data.id),
        ('location', data.location),
        ('social_network1', data.social_network1),
        ('social_network2', data.social_network2),
        ('social_network3', data.social_network3),
        ('social_network4', data.social_network4),
        ('phone_number', data.phone_number),
    ])
