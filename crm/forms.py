from django.forms import ModelForm
from django import forms

from crm.models import Customer, SatisficationDetail
from crm.widgets import AdminImageWidget

class SatisficationDetailForm(ModelForm):
	class Meta:
		model = SatisficationDetail
		fields = ['satisfication', 'point_rate_item', 'value']

	def clean_value(self):
		if self.cleaned_data['value'] > 5 or self.cleaned_data['value'] < 2:
			raise forms.ValidationError('Value can only between 2 to 5')
		return self.cleaned_data['value']


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = [
			'parent',
			'code',
			'name',
			'phone_number',
			'address',
			'city',
			'field',
			'logo',
			'tax_id_number',
			'join_date'
		]

		widgets = {
			'logo': AdminImageWidget
		}