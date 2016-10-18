from django import forms
from django.db.models import Q
from operational.models import PayrollPeriod, Payroll, State
from hrm.models import EmployeeContract

class PayrollPeriodForm(forms.ModelForm):
	class Meta:
		model = PayrollPeriod
		fields = ['start_date', 'end_date']

	def clean_end_date(self):
		if self.cleaned_data['end_date'] < self.cleaned_data['start_date']:
			raise forms.ValidationError('this field must be greater than Start Date')
		return self.cleaned_data['end_date']

class PayrollForm(forms.ModelForm):
	class Meta:
		model = Payroll
		exclude = ['state']

	def clean(self):
		cleaned_data = super(PayrollForm, self).clean()
		if self.is_valid():
			period = cleaned_data['period']
			print(period)
			payroll = Payroll.objects.filter(period=period).filter(Q(state=State.FINAL) \
																  | Q(state=State.PAID))
			print(payroll)
			contracts = [ obj.contract for obj in payroll ]
			print(contracts)
			if cleaned_data['contract'] in contracts:
				#raise forms.ValidationError('Payroll with this Employee Contract \
				#						   and Period already exists')
				msg = "Payroll with this Employee Contract and Period already exists"
				self.add_error('contract', msg)