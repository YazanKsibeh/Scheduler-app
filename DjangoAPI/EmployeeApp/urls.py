from django.urls import include, re_path
from EmployeeApp import views


urlpatterns = [
    re_path(r'^job$',views.job_api),
    re_path(r'^job/([0-9]+)$',views.job_api),
    re_path(r'^employee$',views.employee_api),
    re_path(r'^employee/([0-9]+)$',views.employee_api)
]



