from .import views
from django.urls import path

urlpatterns = (
    path('', views.dashboard, name="dashboard"),
    # path('base', views.base, name='base'),
    path('page', views.page, name='page'),
    path('courses', views.add_courses, name='courses'),
    path('add', views.add_student, name='add'),
    path('billing', views.billing, name="billing"),
    path('profile', views.profile, name="profile"),
    path('rtl', views.rtl, name="rtl"),
    path('sign_in', views.sign_in, name="sign_in"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('tables', views.tables, name="tables"),
    path('virtual_reality', views.virtual_reality, name="virtual_reality"),


    path('create_mentor', views.create_mentor, name='create_mentor'),
    path('update_mentor/<int:pk>', views.update_mentor, name='update_mentor'),
    path('delete_mentor/<int:pk>', views.delete_mentor, name='delete_mentor'),

    path('create_lesson', views.create_lesson, name='create_lesson'),
    path('update_lesson/<int:pk>', views.update_lesson, name='update_lesson'),
    path('delete_lesson/<int:pk>', views.delete_lesson, name='delete_lesson'),

    path('create_group', views.create_group, name='create_group'),
    path('delete_group/<int:pk>', views.delete_group, name='delete_group'),
    path('update_group/<int:pk>', views.update_group, name='update_group'),

    path('add', views.add_student, name='add'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),

)