from django.conf.urls import url

from crm.views import CustomerCreate, CustomerList


urlpatterns = [
    url(r'customer/add/$', CustomerCreate.as_view(), name='customer-add'),
    url(r'customer/$', CustomerList.as_view(), name='customer-list'),
]
