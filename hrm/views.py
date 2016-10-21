from django.shortcuts import render
from django_reporting.utils import Reporting
from django.template import Context
from hrm.models import Employee
import os
# Create your views here.

def employee_report(request):
	employees = Employee.objects.all()
	template = os.getcwd() + '/hrm/template_reports/employee.rml'
	context = Context({'employees': employees})
	report = Reporting(context, template_name=template, output="employee.pdf")
	return report.render()

