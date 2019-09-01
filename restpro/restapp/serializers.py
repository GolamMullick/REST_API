from rest_framework import serializers
from .models import Student
from .models import Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','firstname','lastname')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=('id','name','student','maxstudent')
