from django.contrib import admin
from hrm.models import Division, JobTitle, MaritalStatus, Employee, FamilyOfEmployee, Education, Evaluation, EvaluationItem, EvaluationPeriod, LeaveRecord

# Register your models here.

class FamilyOfEmployeeInline(admin.TabularInline):
	model = FamilyOfEmployee

class EducationInline(admin.StackedInline):
	model = Education
	extra = 0
	fieldsets = (
		('Grade Information', {
			'fields': ('grade', 'graduation_date', 'certificate_number', 'name', 'address', 'city', 'description'),
			'classes': ('collapse')
		}),
	)

class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('reg_number', 'name', 'phone_number' ,'date_of_hire', 'job_title', 'account_number')
	fieldsets = (
		('Personal Information', {
			'fields': ('reg_number', 'id_number', 'name', 'birth_place', 'birth_date', 'address', 'city', 'gender', 'mother_name', 'marital_status')
		}),
		('Other', {
			'fields': ('date_of_hire', 'account_number', 'is_active', 'divison', 'job_title')
		})
	)

	inlines = [
		FamilyOfEmployeeInline, EducationInline
	]

class FamilyOfEmployeeAdmin(admin.ModelAdmin):
	list_display = ('employee', 'name', 'relationship')

class EvaluationPeriodAdmin(admin.ModelAdmin):
	def save_model(self, reques, obj, form, change):
		if obj.evaluation_date:
			if not obj.id:
				if not obj.period:
					obj.period = str(obj.evaluation_date)
		obj.save()

class LeaveRecordAdmin(admin.ModelAdmin):
	list_display = ('date_taken', 'employee')

admin.site.register(Division, DivisionAdmin)
admin.site.register(JobTitle)
admin.site.register(MaritalStatus)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(FamilyOfEmployee, FamilyOfEmployeeAdmin)
admin.site.register(Evaluation)
admin.site.register(EvaluationItem)
admin.site.register(EvaluationPeriod, EvaluationPeriodAdmin)
admin.site.register(LeaveRecord, LeaveRecordAdmin)