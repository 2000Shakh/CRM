from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Lesson


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['fullname', 'age', 'gender', 'email', 'phone', 'spec']


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # widgets = {
        #     'fullname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'age': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gender': forms.Select(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'lesson': forms.Select(attrs={'class': 'form-control'}),
        #     'group': forms.Select(attrs={'class': 'form-control'}),
        #     'payments': forms.Select(attrs={'class': 'form-control'}),
        # }





class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname', 'age', 'gender', 'email', 'phone',  'payment']


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['spec', 'mentor', 'start', 'finish', 'price', 'status']


class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
