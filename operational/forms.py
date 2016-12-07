from django import forms

from operational.models import PayrollPeriod, Payroll


class PeriodChoideField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.id


class PayrollPeriodForm(forms.ModelForm):
    class Meta:
        model = PayrollPeriod
        fields = ['start_date', 'end_date']

    def clean_end_date(self):
        if self.cleaned_data['end_date'] < self.cleaned_data['start_date']:
            raise forms.ValidationError('This field must be greater than Start Date')
        return self.cleaned_data['end_date']


class PayrollCreationForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['period', 'contract']

    def clean_period(self):
        period = self.cleaned_data['period']
        if period.state == "CLOSE":
            raise forms.ValidationError('Cannot add payroll in closed period')
        return period
