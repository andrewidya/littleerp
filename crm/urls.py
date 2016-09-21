from django.conf.urls import url
from crm.views import CustomerCreate

urlpatterns = [
	url(r'customer/add/$', CustomerCreate.as_view(), name='customer-add')
]