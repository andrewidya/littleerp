from django.forms import ModelForm
from django import forms

from hrm.models import EmployeeContract, EvaluationDetail, LeaveTaken, AnnualLeave


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


class LeaveTakenForm(ModelForm):
    class Meta:
        model = LeaveTaken
        exclude = ['id']

    def clean(self):
        cleaned_data = super(LeaveTakenForm, self).clean()
        if self.is_valid():
            if cleaned_data['from_date'].year != cleaned_data['to_date'].year:
                raise forms.ValidationError('Leave date range must be within same year')


class AnnualLeaveForm(ModelForm):
    class Meta:
        model = AnnualLeave
        exclude = ['id']
