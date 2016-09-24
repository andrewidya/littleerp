from django.forms import ModelForm
from adminlte.forms import Bootstrap3DatePicker, BootstrapTextInput, BootstrapRadioSelect, BootstrapNumberInput
from hrm.models import Employee

class EmployeeAddForm(ModelForm):
	class Meta:
		model = Employee
		fields = ('reg_number', 'first_name', 'last_name', 'birth_place', 'birth_date', 'phone_number', 'gender', 'bank_account', 'religion', 'id_number', 'job_title', 'division', 'mother_name', 'blood_type', 'date_of_hire', 'marital_status')
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
			'marital_status': BootstrapRadioSelect()
		}