from django.forms import ModelForm
from hrm.models import Employee, EvaluationDetail, EmployeeContract
from django import forms

class EvaluationDetailForm(ModelForm):
	class Meta:
		model = EvaluationDetail
		exclude = ['id']

	def clean_eval_value(self):
		if self.cleaned_data['eval_value'] > 100:
			raise forms.ValidationError('Unexpected value')
		return self.cleaned_data['eval_value']

class EmployeeContractForm(ModelForm):
	class Meta:
		model = EmployeeContract
		exclude = ['id']
		localize_fields = ('basic_salary',)