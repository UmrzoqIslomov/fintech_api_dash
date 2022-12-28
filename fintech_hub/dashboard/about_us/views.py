import requests as re
from django.shortcuts import render, redirect

from apps.about_us.models.about_us import AboutUsModel
from dashboard.about_us.forms import AboutUsForms


def about_us(requests):
    lists = AboutUsModel.objects.all()
    ctx = {
        'lists': lists
    }
    return render(requests, 'dashboard/about_us/about_us.html', ctx)


def about_form(requests):
    forms = AboutUsForms()
    if requests.POST:
        form = AboutUsForms(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_about_us')
        else:
            print(form.errors)
        return redirect('dash_about_us')
    ctx = {
        "forms": forms
    }
    return render(requests, 'dashboard/about_us/form.html', ctx)


def about_edit(requests, pk):
    if pk:
        root = AboutUsModel.objects.get(pk=pk)
        forms = AboutUsForms(instance=root)
    else:
        raise ValueError('topilmadi 404')
    if requests.POST:
        form = AboutUsForms(requests.POST, requests.FILES or None, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_about_us')
        else:
            print(form.errors)

    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/commend/form.html', ctx)


def delete_about(requests, pk=None, dlt=None):
    if dlt:
        AboutUsModel.objects.get(pk=dlt).delete()
        return redirect("dash_about_us")

    ctg = AboutUsModel.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/about_us/delete.html", ctx)

