from django.forms import ModelForm
from adminlte.forms import Bootstrap3DatePicker, BootstrapTextInput, \
	BootstrapRadioSelect, BootstrapNumberInput, BootstrapCheckbox
from hrm.models import Employee, EvaluationDetail, EmployeeContract
from django import forms

class EmployeeAddForm(ModelForm):
	class Meta:
		model = Employee
		fields = ('reg_number', 'first_name', 'last_name', 'birth_place',
				 'birth_date', 'phone_number', 'gender', 'bank_account',
				 'religion', 'id_number', 'job_title', 'division',
				 'mother_name', 'blood_type', 'date_of_hire',
				 'marital_status', 'is_active')
		widgets = {
			'reg_number': BootstrapTextInput(),
			'first_name': BootstrapTextInput(),
			'last_name': BootstrapTextInput(),
			'birth_place': BootstrapTextInput(),
			'birth_date': Bootstrap3DatePicker(),
			'phone_number': BootstrapTextInput(),
			'gender': BootstrapRadioSelect(),
			'bank_account': BootstrapTextInput(),
			'religion': BootstrapTextInput(),
			'id_number': BootstrapTextInput(),
			'job_title': BootstrapRadioSelect(),
			'division': BootstrapRadioSelect(),
			'mother_name': BootstrapTextInput(),
			'blood_type': BootstrapRadioSelect(),
			'date_of_hire': Bootstrap3DatePicker(),
			'marital_status': BootstrapRadioSelect(),
			'is_active': BootstrapCheckbox()
		}

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