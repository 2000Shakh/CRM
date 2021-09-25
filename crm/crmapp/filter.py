import django_filters
from .models import *


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['full_name', 'birth_date']


class MentorFilter(django_filters.FilterSet):
    class Meta:
        model = Mentor
        fields = '__all__'


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = '__all__'


class LessonFilter(django_filters.FilterSet):
    class Meta:
        model = Lesson
        fields = '__all__'
