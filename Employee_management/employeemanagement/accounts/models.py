from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
\
# Create your models here.

class Employees(models.Model):
    employee_name = models.CharField(max_length = 150)
    employee_profile=models.CharField(max_length=150)
    department=models.CharField(max_length=250,null=True)
    location=models.CharField(max_length=250,null=True)
    salary=models.IntegerField()
    bonus=models.IntegerField()
    role=models.CharField(max_length=250,null=False)
    phone=PhoneNumberField()
    hire_date=models.DateTimeField(auto_now=True)
