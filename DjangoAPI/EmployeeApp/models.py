from django.db import models

# Create your models here.


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=255)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_job = models.CharField(max_length=255)
    schedule_date = models.DateField()