from dataclasses import fields
from rest_framework import serializers
from EmployeeApp.models import Employee,Jobs


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('job_id', 'job_name')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id', 'employee_name', 'employee_job', 'schedule_date')