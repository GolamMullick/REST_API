from django.db import models

class Student(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    


class School(models.Model):
    name=models.CharField(max_length=20)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    maxstudent=models.IntegerField(default=100)
