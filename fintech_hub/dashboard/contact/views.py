import requests as re
from django.shortcuts import render, redirect

from apps.contact.models.contact import ContactModel
from dashboard.contact.forms import ContactForm1


def contact_handler(requests):
    root = ContactModel.objects.all()

    ctx = {
        'root': root
    }
    return render(requests, 'dashboard/contact/contact.html', ctx)


def contact_add(requests):
    forms = ContactForm1()
    if requests.POST:
        form = ContactForm1(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_contact')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/contact/form.html', ctx)


def edit(requests, pk):
    if pk:
        root = ContactModel.objects.get(pk=pk)
        forms = ContactForm1(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = ContactForm1(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_contact')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/contact/form.html', ctx)


def del_conf(request, pk, dlt):
    if dlt:
        ContactModel.objects.get(pk=pk).delete()
        return redirect('#')

    ctg = ContactModel.objects.get(pk=pk)
    ctx = {
        'ctg': ctg
    }

    return render(request, 'dashboard/contact/form.html', ctx)


def delete_contact(requests, pk=None, dlt=None):
    if dlt:
        ContactModel.objects.get(pk=dlt).delete()
        return redirect("dash_contact")

    ctg = ContactModel.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/contact/delete.html", ctx)
