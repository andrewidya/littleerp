from django.views.generic.edit import CreateView
from crm.forms import CustomerAddForm
from crm.models import Customer

# Create your views here.
class CustomerCreate(CreateView):
	model = Customer
	form_class = CustomerAddForm
	template_name = 'crm/customer_add.html'