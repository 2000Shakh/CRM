from typing import Dict

from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentCreateForm
from .filter import *
from django.contrib.auth.decorators import login_required


# def base(request):
#     if request.method == "POST":
#         form = CoursesForm
#         if form.is_valid():
#             form.save()
#             return redirect("base.html")
#         else:
#             form = CoursesForm()
#         context = {
#             'form': form
#         }
#     return render(request, "crmapp/dashboard.html", context)


def page(request):
    return render(request, 'crmapp/page.html')


def add_courses(request):
    form = CoursesForm
    if request.method == "POST":
        form = CoursesForm
        if form.is_valid():
            form.save()
            return redirect("profile.html")
        else:
            form = CoursesForm()
    context = {
        'form': form
        }
    return render(request, "crmapp/courses.html", context)


def dashboard(request):
    return render(request, 'crmapp/dashboard.html')


def tables(request):
    return render(request, 'crmapp/tables.html')


def billing(request):
    return render(request, 'crmapp/billing.html')


def profile(request):
    return render(request, 'crmapp/profile.html')


def rtl(request):
    return render(request, 'crmapp/rtl.html')


def sign_in(request):
    return render(request, 'crmapp/sign_in.html')


def sign_up(request):
    return render(request, 'crmapp/sign_up.html')


def virtual_reality(request):
    return render(request, 'crmapp/virtual_reality.html')


def add_student(request):
    form = StudentRegistrationForm
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tables")
        else:
            form = StudentRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'crmapp/add_students.html', context)


def tables(request):
    mentors = Mentor.objects.all()
    students = Student.objects.all()
    students_qty = students.count()
    f_students = Student.objects.order_by(gender='F')
    f_students_qty = f_students.count()
    group = Group.objects.all()
    lesson = Lesson.objects.all()

    studentFilter = StudentFilter(request.GET, queryset=students)
    students = studentFilter.qs

    mentorFilter = MentorFilter(request.GET, queryset=mentors)
    mentors = mentorFilter.qs

    groupFilter = GroupFilter(request.GET, queryset=group)
    group = groupFilter.qs

    lessonFilter = LessonFilter(request.GET, queryset=lesson)
    lesson = lessonFilter.qs


    context = {
        "mentors": mentors,
        "students": students,
        'group': group,
        'lesson': lesson,
        'studentFilter': studentFilter,
        'mentorFilter': mentorFilter,
        'groupFilter': groupFilter,
        'lessonFilter': lessonFilter,
        'students_qty':students_qty,
        'f_students': f_students,
        'f_students_qty' : f_students_qty,

        # "Filter": Filter,
    }
    return render(request, 'crmapp/tables.html', context)


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentRegistrationForm(instance=student)
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form": form,
    }

    return render(request, "crmapp/add_students.html", context)


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('tables')

    context = {
        "student": student
    }

    return render(request, 'crmapp/delete_student.html', context)

    # mentor = Mentor.objects.get(id=pk)
    # if request.method == 'POST':
    #     mentor.delete()
    #     return redirect('tables')
    #
    # context = {
    #     "mentor": mentor
    # }
    #
    # return render(request, 'crmapp/delete_mentor.html', context)


def create_mentor(request):
    form = MentorCreateForm()
    if request.method == "POST":
        form = MentorCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = MentorCreateForm()

    context = {
        "form": form
    }
    return render(request, "crmapp/create_mentor.html", context)


def update_mentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    form = MentorCreateForm(instance=mentor)
    if request.method == "POST":
        form = MentorCreateForm(request.POST, instance=mentor)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form": form,
    }

    return render(request, "crmapp/create_mentor.html", context)


def delete_mentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == 'POST':
        mentor.delete()
        return redirect('tables')

    context = {
        "mentor": mentor
    }

    return render(request, 'crmapp/delete_mentor.html', context)



def create_group(request):
    form = GroupCreateForm()
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = GroupCreateForm()

    context = {
        "form": form
    }
    return render(request, "crmapp/create_group.html", context)


def update_group(request, pk):
    group = Group.objects.get(id=pk)
    form = GroupCreateForm(instance=group)
    if request.method == "POST":
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form": form
    }

    return render(request, "crmapp/create_group.html", context)


def delete_group(request, pk):
    group1 = Group.objects.get(id=pk)
    if request.method == 'POST':
        group1.delete()
        return redirect('tables')

    context = {
        "group1": group1
    }

    return render(request, 'crmapp/delete_group.html', context)


def create_lesson(request):
    form = LessonCreateForm()
    if request.method == "POST":
        form = LessonCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = LessonCreateForm()

    context = {
        "form": form
    }
    return render(request, "crmapp/create_lesson.html", context)


def update_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonCreateForm(instance=lesson)
    if request.method == "POST":
        form = LessonCreateForm(request.POST, instance=lesson)
        if form.is_valid:
            form.save()
            return redirect('tables')
    context = {
        "form": form
    }
    return render(request, "crmapp/create_lesson.html", context)


def delete_lesson(request, pk):
    lesson1 = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        lesson1.delete()
        return redirect('tables')

    context = {
        "lesson1": lesson1
    }

    return render(request, 'crmapp/delete_lesson.html', context)


