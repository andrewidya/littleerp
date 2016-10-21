from django.conf.urls import url
from hrm import views

urlpatterns = [
	url(r'^report/employee/$', views.employee_report),
]