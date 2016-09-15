from django.contrib import admin
from operation.models import TrainingType, Training, VisitEvaluationSubject, VisitRecord, Visit, TrainingAttendance

# Register your models here.

class TrainingAttendanceInline(admin.TabularInline):
	model = TrainingAttendance

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
	list_display = ('date', 'author', 'subject', 'is_certificate')
	inlines = [
		TrainingAttendanceInline,
	]

@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
	pass

class VisitRecordInline(admin.TabularInline):
	model = VisitRecord

class VisitAdmin(admin.ModelAdmin):
	list_display = ('date', 'customer', 'visitor')
	inlines = [VisitRecordInline]

admin.site.register(VisitEvaluationSubject)
admin.site.register(Visit, VisitAdmin)