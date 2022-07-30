from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=50,primary_key=True)
    emp_img=models.ImageField(upload_to='profilepics',null=True)
    employee_name=models.CharField(max_length=80)
    designation=models.CharField(max_length=80)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    experience=models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.employee_name
