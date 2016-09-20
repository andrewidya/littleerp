from django.contrib import admin
from hrm.models import Division, JobTitle, Employee, FamilyOfEmployee, EmployeeAddress, Education, AnnualLeave, LeaveTaken, LeaveType

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

class AddressInline(admin.TabularInline):
	model = EmployeeAddress

class EducationInline(admin.TabularInline):
	model = Education

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	inlines = [FamilyInline, AddressInline, EducationInline]

@admin.register(AnnualLeave)
class AnnualLeaveAdmin(admin.ModelAdmin):
	pass

@admin.register(LeaveTaken)
class LeaveTakenAdmin(admin.ModelAdmin):
	fields = (('employee', 'leave_type'), ('from_date', 'to_date'), 'day')

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
	pass