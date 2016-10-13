from django.contrib import admin
from hrm.models import Division, JobTitle, Employee, FamilyOfEmployee, \
	EmployeeAddress, Education, AnnualLeave, LeaveTaken, LeaveType, \
	SalaryCategory, SalaryName, EmployeeContract, OtherSalary, BankName, \
	EvaluationDetail, EvaluationPeriod, EvaluationItem, Evaluation
from hrm.forms import EmployeeAddForm, EvaluationDetailForm, \
	EmployeeContractForm
from import_export.admin import ImportExportMixin, ImportMixin

@admin.register(Division)
class DivisionAdmin(ImportExportMixin, admin.ModelAdmin):
	pass

@admin.register(JobTitle)
class JobTitle(ImportExportMixin, admin.ModelAdmin):
	pass

# Employee Inline Formset
class FamilyInline(admin.TabularInline):
	model = FamilyOfEmployee
	extra = 2
	fields = ('name', 'birth_place', 'birth_date', 'gender', 'relationship')
	classes = ('grp-collapse grp-closed',)

class AddressInline(admin.TabularInline):
	model = EmployeeAddress
	extra = 2
	fields = ('address', 'city', 'province', 'address_status')
	classes = ('grp-collapse grp-closed',)

class EducationInline(admin.TabularInline):
	model = Education
	fields = ('grade', 'name', 'city', 'graduation_date')
	classes = ('grp-collapse grp-closed',)

@admin.register(Employee)
class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
	search_fields = ['first_name', 'last_name', 'reg_number']
	list_filter = ('job_title', 'division', 'marital_status')
	list_display = ('reg_number', 'get_full_name', 'gender', 'marital_status',
				   'job_title', 'is_active')
	fieldsets = (
		('Personal Info', {
			'fields': (
				('id_number', 'first_name'), ('phone_number', 'last_name',),
				('birth_place', 'religion'),
				('birth_date', 'gender', 'blood_type'),
				('mother_name', 'marital_status')
			)
		}),
		('Employemnt Info', {
			'fields': (
				('job_title', 'division'), ('reg_number', 'date_of_hire'),
				'is_active', ('bank', 'bank_account')
			)
		}),
	)
	raw_id_fields = ('bank', 'job_title', 'division')
	autocomplete_lookup_fields = {
		'fk': ['bank', 'job_title', 'division'],
	}
	inlines = [FamilyInline, AddressInline, EducationInline]
	list_per_page = 20
	change_list_template = "admin/change_list_filter_sidebar.html"

@admin.register(AnnualLeave)
class AnnualLeaveAdmin(admin.ModelAdmin):
	raw_id_fields = ('employee',)
	autocomplete_lookup_fields = {
		'fk': ['employee'],
	}

@admin.register(LeaveTaken)
class LeaveTakenAdmin(admin.ModelAdmin):
	fields = (('employee', 'leave_type'), ('from_date', 'to_date'), 'day')
	raw_id_fields = ('employee',)
	autocomplete_lookup_fields = {
		'fk': ['employee'],
	}

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	list_display = ('grade', 'employee', 'name', 'address', 'city',
				   'graduation_date', 'certificate')

@admin.register(SalaryCategory)
class SalaryCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
	pass

@admin.register(SalaryName)
class SalaryNameAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ('name', 'salary_category', 'calculate_condition')

#@admin.register(OtherSalary)
#class OtherSalaryAdmin(admin.ModelAdmin):
#	list_display = ('employee_contract', 'salary_name', 'value')
#	raw_id_fields = ('employee_contract',)
#	autocomplete_lookup_fields = {
#		'fk': ['employee_contract']
#	}

class OtherSalaryInline(admin.TabularInline):
	model = OtherSalary
	fields = ('salary_name', 'value')
	raw_id_fields = ('salary_name',)
	autocomplete_lookup_fields = {
		'fk': ['salary_name'],
	}
	classes = ('grp-collapse grp-open',)


@admin.register(EmployeeContract)
class EmployeeContract(admin.ModelAdmin):
	list_display = ('employee', 'service_related', 'start_date', 'end_date',
				   'reference', 'contract_status')
	fieldsets = (
		('Contract Details', {
			'fields': (
				('employee', 'service_related'), ('start_date', 'end_date'),
				('base_salary', 'reference')
			)
		}),
	)
	raw_id_fields = ('employee', 'service_related',)
	autocomplete_lookup_fields = {
		'fk': ['employee', 'service_related'],
	}
	inlines = [OtherSalaryInline]
	search_fields = ('employee__first_name',)
	list_filter = ('contract_status',)
	form = EmployeeContractForm

@admin.register(BankName)
class BankAdmin(ImportMixin, admin.ModelAdmin):
	list_display = ('id', 'name')
	list_per_page = 20
	ordering = ['id']

#@admin.register(EvaluationItem)
#class EvaluationItemAdmin(admin.ModelAdmin):
#	pass

@admin.register(EvaluationPeriod)
class EvaluationPeriodAdmin(admin.ModelAdmin):
	pass

class EvaluationDetailInline(admin.TabularInline):
	model = EvaluationDetail
	form = EvaluationDetailForm

#@admin.register(EvaluationDetail)
#class EvaluationDetailAdmin(admin.ModelAdmin):
#	form = EvaluationDetailForm

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
	fields = (('eval_period', 'date_create'), 'employee')
	list_display = ('eval_period', 'date_create', 'employee', 'ranking')
	raw_id_fields = ('employee',)
	autocomplete_lookup_fields = {
		'fk': ['employee'],
	}
	inlines = [EvaluationDetailInline]