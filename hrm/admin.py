from django.contrib import admin
from hrm.models import Division, JobTitle, Employee, FamilyOfEmployee, EmployeeAddress, Education, AnnualLeave, LeaveTaken, LeaveType, SalaryCategory, SalaryName, EmployeeContract, OtherSalary, BankName
from hrm.forms import EmployeeAddForm
from import_export.admin import ImportExportMixin, ImportMixin

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
	pass

@admin.register(JobTitle)
class JobTitle(admin.ModelAdmin):
	pass

# Employee Inline Formset
class FamilyInline(admin.TabularInline):
	model = FamilyOfEmployee
	extra = 3
	fields = ('name', 'birth_place', 'birth_date', 'gender', 'relationship')

class AddressInline(admin.TabularInline):
	model = EmployeeAddress
	extra = 2
	fields = ('address', 'city', 'province', 'address_status')

class EducationInline(admin.TabularInline):
	model = Education
	fields = ('grade', 'name', 'city', 'graduation_date')

@admin.register(Employee)
class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
	search_fields = ['first_name']
	list_filter = ('job_title', 'division')
	list_display = ('reg_number', 'get_full_name', 'phone_number', 'gender', 'marital_status', 'job_title', 'division', 'date_of_hire', 'is_active')
	fieldsets = (
		('Personal Info', {
			'fields': (('id_number', 'first_name'), ('phone_number', 'last_name',), ('birth_place', 'religion'), ('birth_date', 'gender', 'blood_type'), ('mother_name', 'marital_status'))
		}),
		('Employemnt Info', {
			'fields': (('job_title', 'division', 'date_of_hire'), ('reg_number', 'bank'), ('bank_account', 'is_active'))
		}),
	)
	raw_id_fields = ('bank', 'job_title', 'division')
	autocomplete_lookup_fields = {
		'fk': ['bank', 'job_title', 'division'],
	}
	inlines = [FamilyInline, AddressInline, EducationInline]
	change_list_template = "admin/change_list_filter_sidebar.html"

@admin.register(AnnualLeave)
class AnnualLeaveAdmin(admin.ModelAdmin):
	raw_id_fields = ('employee',)
	autocomplete_lookup_fields = {
		'fk': ['employee']
	}

@admin.register(LeaveTaken)
class LeaveTakenAdmin(admin.ModelAdmin):
	fields = (('employee', 'leave_type'), ('from_date', 'to_date'), 'day')

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	list_display = ('grade', 'employee', 'name', 'address', 'city', 'graduation_date', 'certificate')

@admin.register(SalaryCategory)
class SalaryCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(SalaryName)
class SalaryNameAdmin(admin.ModelAdmin):
	list_display = ('name', 'salary_category', 'calculate_condition')

@admin.register(OtherSalary)
class OtherSalaryAdmin(admin.ModelAdmin):
	list_display = ('employee_contract', 'salary_name', 'value')
	raw_id_fields = ('employee_contract',)
	autocomplete_lookup_fields = {
		'fk': ['employee_contract']
	}

@admin.register(EmployeeContract)
class EmployeeContract(admin.ModelAdmin):
	list_display = ('employee', 'service_related', 'start_date', 'end_date', 'contract_status', 'get_basic_salary', 'reference')
	fields = (('employee', 'service_related'), ('start_date', 'end_date', 'reference'), ('basic_salary', 'contract_status'))
	raw_id_fields = ('employee', 'service_related',)
	autocomplete_lookup_fields = {
		'fk': ['employee', 'service_related'],
	}

@admin.register(BankName)
class BankAdmin(ImportMixin, admin.ModelAdmin):
	pass