from fsm_admin.mixins import FSMTransitionMixin

from django.contrib import admin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.admin.options import IS_POPUP_VAR

from operational.models import (VisitCustomer, VisitPointRateItem,
                                VisitCustomerDetail, PayrollPeriod, Attendance,
                                Payroll, PayrollDetail, PayrollState,
                                PeriodState, CourseType, Course,
                                TrainingSchedule, TrainingClass)
from operational.forms import PayrollCreationForm, PayrollPeriodForm


class VisitCustomerDetailInline(admin.TabularInline):
    model = VisitCustomerDetail
    extra = 1


@admin.register(VisitCustomer)
class VisitCustomerAdmin(admin.ModelAdmin):
    list_display = (
        'visit_date',
        'sales_order_reference',
        'get_customer_name',
        'subject'
    )
    fieldsets = (
        ('Visit Information', {
            'fields': (
                ('subject', 'sales_order_reference'),
                'visit_date',
                'employee'
            )
        }),
    )
    inlines = [VisitCustomerDetailInline]
    filter_horizontal = ('employee',)


@admin.register(VisitPointRateItem)
class VisitPointRateItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    fields = (
        ('employee', 'period'),
        ('work_day', 'sick_day'),
        ('alpha_day', 'leave_day'),
        'leave_left',
    )
    list_display = (
        'period',
        'employee',
        'work_day',
        'sick_day',
        'alpha_day',
        'leave_day',
        'leave_left',
        'staff'
    )
    list_filter = ('period__period', )
    list_select_related = ('employee', 'period', 'staff')

    def save_model(self, request, obj, form, change):
        if obj.staff is None:
            obj.staff = request.user
        obj.save()
        super(AttendanceAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.period.state == PeriodState.CLOSE:
            return ('work_day', 'sick_day', 'alpha_day', 'leave_day',
                    'leave_left', 'employee', 'period')
        return super(AttendanceAdmin, self).get_readonly_fields(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.period.state == PeriodState.CLOSE:
                return False
        return True


class PayrollDetailInline(admin.TabularInline):
    model = PayrollDetail

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.state != PayrollState.DRAFT:
            return ('salary', 'value', 'note')
        return super(PayrollDetailInline, self).get_readonly_fields(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.state != PayrollState.DRAFT:
            return False
        return super(PayrollDetailInline, self).has_delete_permission(request, obj)


@admin.register(Payroll)
class PayrollAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fields = (
        'period',
        'contract',
        'base_salary',
        'overtime',
        'back_pay',
        'base_salary_per_day',
        'normal_overtime',
    )
    list_display = (
        'period',
        'contract',
        'base_salary',
        'base_salary_per_day',
        'overtime',
        'back_pay',
        'normal_overtime',
        'calculate_total',
        'staff',
        'state'
    )
    list_filter = ('period__period', )
    fsm_field = ['state', ]
    actions = ['make_final', 'make_paid']
    list_select_related = True
    add_form = PayrollCreationForm
    inlines = [PayrollDetailInline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'staff', None) is None:
            obj.staff = request.user
        obj.save()
        super(PayrollAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = Payroll.processing_payroll.all()
        if request.user.is_superuser:
            return queryset
        if request.user.has_perm('operational.audit_payroll'):
            return queryset.filter(state=PayrollState.FINAL)
        return queryset.filter(staff=request.user)

    def get_form(self, request, obj=None, **kwargs):
        # defaults = {}
        # if obj is None:
        #     defaults['form'] = self.add_form
        # defaults.update(kwargs)
        # return super(PayrollAdmin, self).get_form(request, obj, **defaults)
        if obj is None:
            return self.add_form
        return super(PayrollAdmin, self).get_form(request, obj, **kwargs)

    def get_fields(self, request, obj=None):
        if not obj:
            return ('period', 'contract')
        return super(PayrollAdmin, self).get_fields(request, obj)

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        return [inline(self.model, self.admin_site) for inline in self.inlines]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.state != PayrollState.DRAFT:
            return ('period', 'contract', 'base_salary', 'overtime', 'back_pay',
                    'base_salary_per_day', 'normal_overtime')
        return super(PayrollAdmin, self).get_readonly_fields(request, obj=obj)

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST['_continue'] = 1
        return super(PayrollAdmin, self).response_add(request, obj, post_url_continue)

    def make_final(self, request, queryset):
        for obj in queryset:
            if obj.state == PayrollState.FINAL:
                continue
            obj.total = obj.calculate_total()
            obj.state = PayrollState.FINAL
            obj.save()
    make_final.short_description = 'Mark selected payroll as final'

    def make_paid(self, request, queryset):
        queryset.update(state=PayrollState.PAID)
    make_paid.short_description = 'Mark selected payroll item as paid'

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.state == PayrollState.PAID:
            return False
        return True

    def get_actions(self, request):
        actions = super(PayrollAdmin, self).get_actions(request)
        if request.user.is_superuser:
            return actions

        if not request.user.has_perm('operational.pay_payroll'):
            if 'make_paid' in actions:
                del actions['make_paid']
        else:
            if 'make_final' in actions:
                del actions['make_final']
                del actions['delete_selected']
        return actions

    def response_change(self, request, obj):
        super(PayrollAdmin, self).response_change(request, obj)
        changelist_url = reverse('admin:operational_payroll_changelist')
        return redirect(changelist_url)


@admin.register(PayrollPeriod)
class PayrollPeriodAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = (
        'period',
        'date_create',
        'start_date',
        'end_date',
        'state'
    )
    fieldsets = (
        ('Period Information', {
            'fields': (('start_date', 'end_date'), 'state')
        }),
    )
    readonly_fields = ('state', )
    list_filter = ('period', )
    form = PayrollPeriodForm

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if obj.state == PeriodState.CLOSE:
                return ('start_date', 'end_date', 'state')
        return self.readonly_fields


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_select_related = True


@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
    list_select_related = ('course', 'course__course_type')


@admin.register(TrainingClass)
class TrainingClassAdmin(admin.ModelAdmin):
    list_select_related = ('schedule', 'employee')
