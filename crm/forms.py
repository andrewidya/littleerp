from django.forms import ModelForm
from crm.models import Customer, SatisficationDetail
from adminlte.forms import Bootstrap3DatePicker, BootstrapTextInput, BootstrapRadioSelect
from django import forms

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

class SatisficationDetailForm(ModelForm):
	class Meta:
		model = SatisficationDetail
		fields = ['satisfication', 'point_rate_item', 'value']

	def clean_value(self):
		if self.cleaned_data['value'] > 5 or self.cleaned_data['value'] < 2:
			raise forms.ValidationError('Unexpected value')
		return self.cleaned_data['value']