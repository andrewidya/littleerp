from django.contrib import admin
from operation.models import TrainingType, Training, VisitEvaluationSubject, VisitRecord, Visit

# Register your models here.

class TrainingAdmin(admin.ModelAdmin):
	list_display = ('date', 'author', 'employee', 'is_certificate')

class VisitRecordInline(admin.TabularInline):
	model = VisitRecord

class VisitAdmin(admin.ModelAdmin):
	list_display = ('date', 'customer', 'branch', 'visitor')
	inlines = [VisitRecordInline]

admin.site.register(Training, TrainingAdmin)
admin.site.register(VisitEvaluationSubject)
admin.site.register(Visit, VisitAdmin)