from django.forms import ModelForm
from crm.models import Customer, SatisficationDetail
from django import forms

class SatisficationDetailForm(ModelForm):
	class Meta:
		model = SatisficationDetail
		fields = ['satisfication', 'point_rate_item', 'value']

	def clean_value(self):
		if self.cleaned_data['value'] > 5 or self.cleaned_data['value'] < 2:
			raise forms.ValidationError('Unexpected value')
		return self.cleaned_data['value']