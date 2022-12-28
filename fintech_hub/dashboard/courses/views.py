from django.shortcuts import render, redirect

from apps.courses.models.courses import CourseModel
from dashboard.courses.forms import CourseForm
from dashboard.courses.service import get_courses


def courses_lists(requests, pk=None):
    root = CourseModel.objects.all()
    ctx = {
        'root': root
    }

    return render(requests, f'dashboard/courses/courses.html', ctx)


def add(requests):
    forms = CourseForm()
    if requests.POST:
        form = CourseForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_courses')
    ctx = {
        'forms': forms
    }
    return render(requests, f'dashboard/courses/form.html', ctx)


def edit(requests, pk):
    if pk:
        root = CourseModel.objects.get(pk=pk)
        forms = CourseForm(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = CourseForm(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_courses')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, "dashboard/courses/form.html", ctx)


def delete_courses(requests, pk=None, dlt=None):
    if dlt:
        CourseModel.objects.get(pk=dlt).delete()
        return redirect("dash_tables")

    ctg = CourseModel.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/courses/delete.html", ctx)