from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
     path('student_table/',views.student_table, name = 'student_table'),
]