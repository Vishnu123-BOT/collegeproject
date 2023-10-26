from  django.db import models
from django .urls import reverse


class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='Department', blank=True)



    def __str__(self):
         return self.name
