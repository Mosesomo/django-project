from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullnames = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
