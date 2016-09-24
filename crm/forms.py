from django.forms import ModelForm
from crm.models import Customer
from adminlte.forms import Bootstrap3DatePicker, BootstrapTextInput, BootstrapRadioSelect

class CustomerAddForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('code', 'name', 'phone_number', 'address', 'city', 'field', 'tax_id_number', 'join_date', 'parent')
		widgets = {
			'code': BootstrapTextInput(),
			'name': BootstrapTextInput(),
			'phone_number': BootstrapTextInput(),
			'address': BootstrapTextInput(),
			'city': BootstrapTextInput(),
			'field': BootstrapTextInput(),
			'tax_id_number': BootstrapTextInput(),
			'join_date': Bootstrap3DatePicker(),
			'parent': BootstrapRadioSelect(),
		}
