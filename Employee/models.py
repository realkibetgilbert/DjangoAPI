from django.db import models

# Create your models here.
class Departments(models.Models):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)