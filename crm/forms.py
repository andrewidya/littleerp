from django.forms import ModelForm, TextInput, DateInput
from crm.models import Customer

class CustomerAddForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('code', 'name', 'phone_number', 'address', 'city', 'field', 'tax_id_number', 'join_date')
		widgets = {
			'code': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Customer CODE',
				}
			),
			'name': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Customer Name',
				}
			),
			'phone_number': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Phone Number',
				}
			),
			'address': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Address',
				}
			),
			'city': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'City',
				}
			),
			'field': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Bussiness Type',
				}
			),
			'tax_id_number': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'NPWP',
				}
			),
		}
