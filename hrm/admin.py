from jet.admin import CompactInline

from django.contrib import admin

from hrm.forms import AnnualLeaveForm, EmployeeContractForm, EvaluationDetailForm, LeaveTakenForm
from hrm.models import (AnnualLeave, BankName, Division, Education, Employee, EmployeeAddress, EmployeeContract,
                        Evaluation, EvaluationDetail, EvaluationItem, EvaluationPeriod, FamilyOfEmployee, JobTitle,
                        LeaveTaken, LeaveType, OtherSalary, SalaryCategory, SalaryName)


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    pass


@admin.register(JobTitle)
class JobTitle(admin.ModelAdmin):
    pass


@admin.register(FamilyOfEmployee)
class FamilyAdmin(admin.ModelAdmin):
    report_template = "hrm/report/family.html"
    report_context_object_name = "Families"


class FamilyInline(CompactInline):
    model = FamilyOfEmployee
    extra = 1
    fields = (
        'name',
        'gender',
        'relationship',
        'birth_place',
        'birth_date'
    )
    show_change_link = True


class AddressInline(CompactInline):
    model = EmployeeAddress
    extra = 1
    fields = (
        'address',
        'city',
        'province',
        'address_status'
    )
    show_change_link = True


class EducationInline(CompactInline):
    model = Education
    extra = 1
    fields = (
        'grade',
        'name',
        'city',
        'graduation_date'
    )
    show_change_link = True


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'reg_number']
    list_filter = ('job_title', 'division', 'marital_status')
    list_display = (
        'reg_number',
        'get_full_name',
        'gender',
        'marital_status',
        'job_title',
        'is_active'
    )
    fieldsets = (
        ('Personal Info', {
            'fields': (
                ('id_number', 'first_name'),
                ('phone_number', 'last_name',),
                ('birth_place', 'religion'),
                ('birth_date', 'gender'),
                'blood_type',
                ('mother_name', 'marital_status')
            )
        }),
        ('Employemnt Info', {
            'fields': (
                'reg_number',
                'job_title',
                'division',
                ('date_of_hire', 'is_active'),
                'bank',
                'bank_account'
            )
        }),
    )
    inlines = [FamilyInline, AddressInline, EducationInline]
    list_per_page = 20
    list_select_related = ('division', 'job_title')


@admin.register(AnnualLeave)
class AnnualLeaveAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'leave_type',
        'year',
        'remaining_day_allowed',
        'last_update'
    )
    fields = (
        'employee',
        'leave_type',
        'year',
        'day_allowed'
    )
    list_filter = ('leave_type',)
    search_fields = (
        'employee__first_name',
        'employee__last_name',
        'employee__reg_number'
    )
    form = AnnualLeaveForm


@admin.register(LeaveTaken)
class LeaveTakenAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'leave_type',
        'from_date',
        'to_date',
        'day')
    fields = (
        'employee',
        'leave_type',
        'from_date',
        'to_date',
    )
    list_filter = ('leave_type',)
    search_fields = (
        'employee__first_name',
        'employee__last_name',
        'employee__reg_number'
    )
    form = LeaveTakenForm


@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'grade',
        'employee',
        'name',
        'address',
        'city',
        'graduation_date',
        'certificate'
    )


@admin.register(SalaryCategory)
class SalaryCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SalaryName)
class SalaryNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary_category', 'calculate_condition')


class OtherSalaryInline(admin.TabularInline):
    model = OtherSalary
    fields = ('salary_name', 'value')


@admin.register(EmployeeContract)
class EmployeeContractAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'service_related',
        'start_date',
        'end_date',
        'reference',
        'contract_status'
    )
    fieldsets = (
        ('Contract Details', {
            'fields': (
                'employee', 'service_related', ('start_date', 'end_date'),
                ('base_salary', 'reference')
            )
        }),
    )
    search_fields = (
        'employee__first_name',
        'employee__last_name',
        'employee__reg_number'
    )
    list_filter = ('contract_status',)
    inlines = [OtherSalaryInline]
    form = EmployeeContractForm

    def get_queryset(self, request):
        return EmployeeContract.default_contract_manager.all()


@admin.register(BankName)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 20
    ordering = ['id']


@admin.register(EvaluationPeriod)
class EvaluationPeriodAdmin(admin.ModelAdmin):
    list_display = ('evaluation_date', 'period')


@admin.register(EvaluationItem)
class EvaluationItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class EvaluationDetailInline(admin.TabularInline):
    model = EvaluationDetail
    form = EvaluationDetailForm


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    fields = ('eval_period', 'date_create', 'employee', 'evaluated_location')
    list_display = (
        'employee',
        'evaluated_location',
        'eval_period',
        'date_create',
        'ranking'
    )
    list_filter = ('eval_period__period', 'ranking')
    search_fields = (
        'employee__first_name',
        'employee__last_name',
        'employee__reg_number'
    )
    inlines = [EvaluationDetailInline]
