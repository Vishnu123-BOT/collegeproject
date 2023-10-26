from  django.db import models
from collegestoreapp.models import Department

class Course(models.Model):
    name=models.CharField(max_length=250)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
          return self.name

class Purpose(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=250,unique=True)
    email=models.EmailField()
    DOB=models.DateField()
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)
    phonenumber=models.CharField(max_length=12)
    address=models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    material_provide=models.CharField(max_length=250)

    def __str__(self):
            return  self.name