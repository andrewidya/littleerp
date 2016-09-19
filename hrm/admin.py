from django.contrib import admin
from hrm.models import Division, JobTitle, MaritalStatus, Employee, FamilyOfEmployee, Education, Evaluation, EvaluationItem, EvaluationPeriod, LeaveRecord, SalaryInformation, SalaryItem

# Register your models here.

class FamilyOfEmployeeInline(admin.TabularInline):
	model = FamilyOfEmployee
	fields = ('name', 'birth_place' ,'birth_date', 'relationship')

class EducationInline(admin.StackedInline):
	model = Education
	extra = 0
	fieldsets = (
		('Grade Information', {
			'fields': ('grade', 'graduation_date', 'certificate_number', 'name', 'address', 'city', 'description'),
			'classes': ('collapse')
		}),
	)

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

@admin.register(SalaryItem)
class SalaryItemAdmin(admin.ModelAdmin):
	fields = ('name', 'description')

class SalaryInformationInline(admin.TabularInline):
	model = SalaryInformation
	extra = 4

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('reg_number', 'name', 'gender', 'marital_status', 'phone_number' ,'date_of_hire', 'division', 'job_title', 'bank_account')
	fieldsets = (
		('Personal Information', {
			'fields': ('reg_number', 'id_number', 'name', 'birth_place', 'birth_date', 'address', 'city', 'gender', 'mother_name', 'marital_status')
		}),
		('Other', {
			'fields': ('date_of_hire', 'bank_account', 'is_active', 'division', 'job_title')
		})
	)

	inlines = [
		FamilyOfEmployeeInline, EducationInline, SalaryInformationInline,
	]

@admin.register(FamilyOfEmployee)
class FamilyOfEmployeeAdmin(admin.ModelAdmin):
	list_display = ('employee', 'name', 'relationship')

@admin.register(EvaluationPeriod)
class EvaluationPeriodAdmin(admin.ModelAdmin):
	def save_model(self, reques, obj, form, change):
		if obj.evaluation_date:
			if not obj.id:
				if not obj.period:
					obj.period = str(obj.evaluation_date)
		obj.save()

@admin.register(LeaveRecord)
class LeaveRecordAdmin(admin.ModelAdmin):
	list_display = ('date_taken', 'employee')

@admin.register(SalaryInformation)
class SalaryInformation(admin.ModelAdmin):
	pass

admin.site.register(JobTitle)
admin.site.register(MaritalStatus)
admin.site.register(Evaluation)
admin.site.register(EvaluationItem)