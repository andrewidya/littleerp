from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from crm.forms import CustomerAddForm
from crm.models import Customer


class CustomerCreate(CreateView):
    model = Customer
    form_class = CustomerAddForm
    template_name = 'crm/customer_add.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.has_perm('crm.add_customer'):
            return super(CustomerCreate, self).dispatch(*args, **kwargs)
        return HttpResponseRedirect('/admin/')


class CustomerList(ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'crm/customer_list'

    def get_context_data(self, **kwargs):
        context = super(CustomerList, self).get_context_data(**kwargs)
        return context
