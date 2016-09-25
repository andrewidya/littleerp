from django import forms
from django.utils.safestring import mark_safe

class Bootstrap3DatePicker(forms.TextInput):
	class Media:
		css = {'all': ('adminlte/plugins/datepicker/datepicker3.css',)}

		js = ('adminlte/plugins/datepicker/bootstrap-datepicker.js',)

	def __init__(self, *args, **kwargs):
		kwargs['attrs'] = 	{
			'data-provide': 'datepicker',
			'class': 'form-control pull-right',
			'data-date-format': 'yyyy-mm-dd',
		}
		super(Bootstrap3DatePicker, self).__init__(*args, **kwargs)

	def render(self, name, value, attrs=None):
		output = []
		output.append(u'<div class="input-group date">')
		output.append(u'<div class="input-group-addon">')
		output.append(u'<i class="fa fa-calendar"></i>')
		output.append(u'</div>')
		output.append(super(Bootstrap3DatePicker, self).render(name, value, attrs))
		output.append(u'</div>')
		return mark_safe(u''.join(output))

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

class BootstrapCheckbox(forms.CheckboxInput):
	pass
