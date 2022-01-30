from re import I
from django.shortcuts import render
#this decorator allows other domains to access our API methodes:
from django.views.decorators.csrf import csrf_exempt
# We need JSON Parser to parse incoming data into data model:
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Jobs,Employee
from EmployeeApp.serializers import JobsSerializer,EmployeeSerializer



# API Methodes for Jobs
@csrf_exempt
def job_api(request, id = 0):
    if request.method == 'GET':
        jobs = Jobs.objects.all()
        jobs_serializer = JobsSerializer(jobs, many = True)
        return JsonResponse(jobs_serializer.data, safe=False)
    elif request.method == 'POST':
        job_data = JSONParser().parse(request)
        jobs_serializer = JobsSerializer(data = job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        job_data = JSONParser().parse(request)
        job = Jobs.objects.get(job_id = job_data['job_id'])
        jobs_serializer = JobsSerializer(job, data = job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        job = Jobs.objects.get(job_id = id)
        job.delete()
        return JsonResponse("Deleted Successfully", safe=False)


#API for Employees :
@csrf_exempt
def employee_api(request, id = 0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many = True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data = employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(employee_id = employee_data['employee_id'])
        employees_serializer = JobsSerializer(employee, data = employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(employee_id = id)
        employee.delete()
        return JsonResponse("Employee Deleted Successfully", safe=False)

