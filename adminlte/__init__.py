from django.forms.forms import BoundField
from adminlte.forms import BootstrapRadioSelect

default_app_config = 'adminlte.apps.AdminLTEConfig'

def add_label_control(func):
	def control_label_tag(self, contents=None, attrs=None, label_suffix=None):
		if attrs is None: attrs = {}
		attrs['class'] = ""
		return func(self, contents, attrs, label_suffix)
	return control_label_tag

BoundField.label_tag = add_label_control(BoundField.label_tag)