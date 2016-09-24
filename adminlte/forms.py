from django import forms

class Bootstrap3DatePicker(forms.TextInput):
	class Media:
		css = {'all': ('adminlte/plugins/datepicker/datepicker3.css',)}

		js = ('adminlte/plugins/datepicker/bootstrap-datepicker.js',)

	def __init__(self, *args, **kwargs):
		kwargs['attrs'] = 	{
			'data-provide': 'datepicker',
			'class': 'form-control',
			'data-date-format': 'yyyy-mm-dd',
		}
		super(Bootstrap3DatePicker, self).__init__(*args, **kwargs)

class BootstrapTextInput(forms.TextInput):
	def __init__(self, *args, **kwargs):
		kwargs['attrs'] = {
			'class': 'form-control',
		}
		super(BootstrapTextInput, self).__init__(*args, **kwargs)

class BootstrapRadioSelect(forms.Select):
	def __init__(self, *args, **kwargs):
		kwargs['attrs'] = {
			'class': 'form-control',
		}
		super(BootstrapRadioSelect, self).__init__(*args, **kwargs)

class BootstrapNumberInput(forms.NumberInput):
	def __init__(self, *args, **kwargs):
		kwargs['attrs'] = {
			'class': 'form-control',
		}
		super(BootstrapNumberInput, self).__init__(*args, **kwargs)

