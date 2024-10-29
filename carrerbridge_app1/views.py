from django.shortcuts import render
from django.http import  HttpResponse
from .models import Student

# Create your views here.

def home(request):
    our_dict = {'insert_carrerbridge': "CareerBridge Django Trianing Institutue in KPHB"}
    return render(request, 'carrerbridge_app1/index.html', context=our_dict)

def student_table(request):
    students = Student.objects.all()
    return render(request, 'carrerbridge_app1/student_table.html', {'students':students})


