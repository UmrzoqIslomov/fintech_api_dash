from django.shortcuts import render, redirect

from apps.teachers.models.teachers import TeacherModel
from dashboard.teachers.forms import TeacherForm


def teacher_list(requests):
    lists = TeacherModel.objects.all()
    ctx = {
        'lists': lists
    }
    return render(requests, 'dashboard/teacher/teacher.html', ctx)


def edit_teacher(requests, pk):
    if pk:
        root = TeacherModel.objects.get(pk=pk)
        forms = TeacherForm(instance=root)
    else:
        raise ValueError('Toplimadi 404')
    if requests.POST:
        form = TeacherForm(requests.POST, requests.FILES, instance=root)
        if form.is_valid():
            form.save()
            return redirect('dash_tables')
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }

    return render(requests, 'dashboard/teacher/form.html', ctx)


def add_teacher(requests):
    forms = TeacherForm()
    if requests.POST:
        form = TeacherForm(requests.POST, requests.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dash_tables')
    ctx = {
        'forms': forms
    }
    return render(requests, 'dashboard/teacher/form.html', ctx)


def delete_teacher(requests, pk=None, dlt=None):
    if dlt:
        TeacherModel.objects.get(pk=dlt).delete()
        return redirect("dash_tables")

    ctg = TeacherModel.objects.get(pk=pk)
    ctx = {
        "ctg": ctg
    }
    return render(requests, "dashboard/teacher/delete.html", ctx)
