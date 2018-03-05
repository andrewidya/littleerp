from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from operational.models import PayrollPeriod, Payroll


class PeriodChoideField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.id


class PayrollPeriodForm(forms.ModelForm):
    class Meta:
        model = PayrollPeriod
        fields = ['start_date', 'end_date']

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        if end_date < self.cleaned_data['start_date']:
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


class PayrollProposalReportForm(forms.Form):
    REPORT_CHOICES = (
        (1, 'Pengajuan Payroll'),
        (2, 'Rincian Payroll')
    )
    period = forms.DateField(widget=AdminDateWidget)
    report_type = forms.ChoiceField(required=True, choices=REPORT_CHOICES)
