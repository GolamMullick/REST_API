from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,Teacher
from .serializers import StudentSerializer,TeacherSerializer

class StudentView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class TeacherView(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer




# Create your views here.
