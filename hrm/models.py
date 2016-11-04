from __future__ import division
from django.db import models
from django.utils.translation import ugettext as _
from crm.models import SalesOrderDetail
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.conf import settings
import datetime

# Create your models here.


class BankName(models.Model):
    name = models.CharField(verbose_name=_('Bank Name'), max_length=50)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)


class Division(models.Model):
    name = models.CharField(verbose_name=_('Division Name'), max_length=20)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)


class JobTitle(models.Model):
    name = models.CharField(verbose_name=_('Job Title'), max_length=20)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)


class Employee(models.Model):
    BLODD_TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB')
    )

    GENDER_CHOICES = (
        ('P', 'Perempuan'),
        ('L', 'Laki-laki')
    )

    MARITAL_CHOICES = (
        ('TK', 'Belum Menikah'),
        ('K/0', 'Menikah Anak 0'),
        ('K/1', 'Menikah Anak 1'),
        ('K/2', 'Menikah Anak 2'),
        ('K/3', 'Menikah Anak 3')
    )

    reg_number = models.CharField(verbose_name=_('Registration Number'), max_length=15, unique=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50, blank=True)
    birth_place = models.CharField(verbose_name=_('Birth Place'), max_length=25)
    birth_date = models.DateField(verbose_name=_('Birth Date'))
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15, null=True, blank=True)
    gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER_CHOICES, blank=True)
    bank = models.ForeignKey(BankName, verbose_name=_('Bank'), blank=True, null=True)
    bank_account = models.CharField(verbose_name=_('Bank Account'), max_length=20, null=True, blank=True)
    religion = models.CharField(verbose_name=_('Religion'), max_length=10, blank=True)
    id_number = models.CharField(verbose_name=_('ID Number'), max_length=15, null=True, blank=True)
    job_title = models.ForeignKey(JobTitle, verbose_name=_('Job Tittle'), blank=True, null=True)
    division = models.ForeignKey(Division, verbose_name=_('Division'), blank=True, null=True)
    mother_name = models.CharField(verbose_name=_('Mother Name'), max_length=30, blank=True)
    blood_type = models.CharField(verbose_name=_('Blood Type'), max_length=2, choices=BLODD_TYPE_CHOICES, blank=True)
    date_of_hire = models.DateField(verbose_name=_('Date of Hire'))
    marital_status = models.CharField(verbose_name=_('Marital Status'), max_length=3, choices=MARITAL_CHOICES)
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        permissions = (
            ('hrm_employee_view', 'Can view only'),
        )

    def __str__(self):
        return self.reg_number + " " + self.first_name + " " + self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    get_full_name.short_description = 'Name'
    get_full_name.allow_tags = True

    @staticmethod
    def autocomplete_search_fields():
        return ('first_name', 'last_name', 'reg_number')


class EmployeeAddress(models.Model):
    employee = models.ForeignKey(Employee)
    address = models.CharField(verbose_name=_('Address'), max_length=255)
    district = models.CharField(verbose_name=_('District'), max_length=255)
    city = models.CharField(verbose_name=_('City'), max_length=255)
    province = models.CharField(verbose_name=_('province'), max_length=255)
    address_status = models.CharField(verbose_name=_('Description'), max_length=8,
        choices=(
            ('KTP', 'KTP'),
            ('ASAL', 'ASAL'),
            ('DOMISILI', 'DOMISILI')
        ))

    def __str__(self):
        return self.address


class FamilyOfEmployee(models.Model):
    GENDER_CHOICES = (
        ('P', 'Perempuan'),
        ('L', 'Laki-laki'),
    )

    RELATIONSHIP_CHOICES = (
        ('I', 'Istri'),
        ('S', 'Suami'),
        ('A', 'Anak'),
    )
    employee = models.ForeignKey(Employee)
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    birth_place = models.CharField(verbose_name=_('Birth Place'), max_length=25)
    birth_date = models.DateField()
    id_number = models.CharField(verbose_name=_('ID Number'), max_length=15, null=True, blank=True)
    gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER_CHOICES)
    relationship = models.CharField(verbose_name=_('Relationship'), max_length=1, choices=RELATIONSHIP_CHOICES)
    activity = models.CharField(verbose_name=_('Current Activity'), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Family Information'
        verbose_name_plural = "Familiy Informations"

    def __str__(self):
        return self.employee.get_full_name()

# Education Module


class Education(models.Model):
    GRADE_CHOICES = (
        ('1', 'SD'),
        ('2', 'SMP'),
        ('3', 'SMA/SMK Sederajat'),
        ('4', 'D1'),
        ('5', 'D2'),
        ('6', 'D3'),
        ('7', 'D4/S1'),
        ('8', 'S2/Magister Sederajat'),
        ('9', 'S3/Doktoral'),
        ('10', 'Akademi/Pelatihan'),
    )

    employee = models.ForeignKey(Employee)
    grade = models.CharField(verbose_name=_('Grade'), max_length=2, choices=GRADE_CHOICES)
    name = models.CharField(verbose_name=_('Institution Name'), max_length=50)
    address = models.CharField(verbose_name=_('Address'), max_length=100, blank=True)
    city = models.CharField(verbose_name=_('City'), max_length=25, blank=True)
    graduation_date = models.DateField()
    certificate = models.BooleanField(default=False)
    certificate_number = models.CharField(verbose_name=_('Certificate Number'), max_length=30, blank=True)
    description = models.CharField(verbose_name=_('Short Description'), max_length=255, blank=True)

    class Meta:
        verbose_name = 'Education'

    def __str__(self):
        return Education.GRADE_CHOICES[int(self.grade)-1][1]

# Leave Module


class LeaveType(models.Model):
    name = models.CharField(verbose_name=_('Leave Type'), max_length=50, help_text="Ex: Medical, Holliday etc")

    class Meta:
        verbose_name = 'Leave Type'
        verbose_name_plural = 'Leave Types'

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains',)


class AnnualLeave(models.Model):
    employee = models.ForeignKey(Employee)
    leave_type = models.ForeignKey(LeaveType)
    year = models.DateField(verbose_name=_('Year'));
    day_allowed = models.SmallIntegerField(verbose_name=_('Day Allowed'), null=True, blank=True)
    remaining_day_allowed = models.SmallIntegerField(verbose_name=_('Remainig Days'), null=True, blank=True)
    last_update = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Annual Leave'
        verbose_name_plural = 'Annual Leaves'

    def __str__(self):
        return self.employee.get_full_name()


class LeaveTaken(models.Model):
    employee = models.ForeignKey(Employee)
    leave_type = models.ForeignKey(LeaveType)
    from_date = models.DateField()
    to_date = models.DateField()
    day = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Leave Check List'
        verbose_name_plural = 'Leave Check Lists'

    def __str__(self):
        return self.employee.get_full_name()

    def save(self, *args, **kwargs):
        diff = self.to_date - self.from_date
        self.day = diff.days
        super(LeaveTaken, self).save(*args, **kwargs)

# Evaluation Module


class EvaluationPeriod(models.Model):
    evaluation_date = models.DateField()
    period = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Evaluation Period'

    def __str__(self):
        return self.period

    def save(self, *args, **kwargs):
        if self.id == None:
            self.period = str(self.evaluation_date.month) + "-" + str(self.evaluation_date.year)
        super(EvaluationPeriod, self).save(*args, **kwargs)


class EvaluationItem(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Evaluating Item'
        verbose_name_plural = 'Evaluating Items'

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    date_create = models.DateField(verbose_name=_('Date Created'))
    employee = models.ForeignKey(Employee, verbose_name=_('Employee Name'))
    eval_period = models.ForeignKey(EvaluationPeriod, verbose_name=_('Period'))
    ranking = models.CharField(verbose_name=_('Ranking'), max_length=6)

    def __str__(self):
        return self.employee.first_name

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'

    def evaluation_rate(self):
        rate = 0
        rate_count = 0
        self.evaluationdetail_set.all()
        for evaluation in self.evaluationdetail_set.all():
            if evaluation.eval_item:
                rate_count += (1 * 1.0)
                rate += (evaluation.eval_value * 1.0)
        ranking = rate / rate_count
        if ranking <= 50:
            self.ranking = "BURUK"
        elif ranking <= 70:
            self.ranking = "CUKUP"
        else:
            self.ranking = "BAIK"


class EvaluationDetail(models.Model):
    evaluation = models.ForeignKey(Evaluation)
    eval_item = models.ForeignKey(EvaluationItem, verbose_name=_('Point Item'))
    eval_value = models.PositiveIntegerField(verbose_name=_('Point Value'))

    class Meta:
        verbose_name = 'Evaluation Detail'
        verbose_name_plural = 'Evaluation Details'
        unique_together = ('evaluation', 'eval_item')

# model for dealing with salary of employee related to
# detail of sales order created by sales (CRM Application)


class SalaryCategory(models.Model):
    name = models.CharField(verbose_name=_('Salary Category'), max_length=255)

    class Meta:
        verbose_name = 'Salary Category'
        verbose_name_plural = 'Salary Categories'

    def __str__(self):
        return self.name


class SalaryName(models.Model):
    CALCULATE_CHOICES = (
            ('+', 'Adding Total Salary'),
            ('-', 'Decreasing Total Salary')
    )

    name = models.CharField(verbose_name=_('Salary Name'), max_length=255)
    salary_category = models.ForeignKey(SalaryCategory, related_name='salary_category', on_delete=models.PROTECT)
    calculate_condition = models.CharField(verbose_name=_('Calculating Condition'), choices=CALCULATE_CHOICES,
                                           help_text=_('Condition needed for calculate total salary'), max_length=1)

    class Meta:
        verbose_name = 'Salary Name'
        verbose_name_plural = 'Salaries Name'

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains', 'salary_category__name__icontains')


class EmployeeContract(models.Model):
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'), related_name='contract')
    service_related = models.ForeignKey(SalesOrderDetail, verbose_name=_('Customer Demand Related'),
                                        related_name='service_order',
                                        help_text=_('This info related to the service needed by customer as detail of \
                                                    sales order'))
    contract_status = models.CharField(blank=True, max_length=8, default="ACTIVE")
    base_salary = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Basic Salary'),
        null=True, blank=True)
    reference = models.CharField(blank=True, max_length=255)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return str(self.employee) + " " + str(self.service_related)

    def get_basic_salary(self):
        return self.basic_salary
    get_basic_salary.short_description = 'Basic Salary'

    @staticmethod
    def autocomplete_search_fields():
        return ('employee__first_name__icontains', 'reference__icontains',
                'service_related__sales_order__number__icontains')

    def get_contract_salary(self):
        salaries = 0
        if not self.contract_status == "ACTIVE":
            return "IDR{:,.2f}".format(salaries)
        for other in self.other_salary.all():
            if other.salary_name.calculate_condition == "+":
                salaries += other.value
            else:
                salaries -= other.value
        return 'IDR{:,.2f}'.format(salaries)
    get_contract_salary.short_description = 'Other Salaries in Contract'

    def get_salaries_in_contract(self):
        list_salaries = ""
        for other in self.other_salary.all():
            list_salaries += "<li>- {0}</li>".format(other.salary_name)
        return mark_safe("<ol>{0}</ol>".format(list_salaries))

    get_salaries_in_contract.short_description = 'Other Salaries Detials'
    get_salaries_in_contract.allow_tags = True

    def check_contract_status(self):
        today = timezone.now()
        warning_level = today + datetime.timedelta(
                days=settings.MINIERP_SETTINGS['HRM']['recontract_warning'])
        if self.end_date < today.date():
            return "EXPIRED"
        if today.date() <= self.end_date <= warning_level.date():
            return "NEED RENEWAL"
        return "ACTIVE"


class OtherSalary(models.Model):
    employee_contract = models.ForeignKey(EmployeeContract, verbose_name=_('Employee Contract'), related_name='other_salary')
    salary_name = models.ForeignKey(SalaryName, verbose_name=_('Salary Name'), related_name='salary_name')
    value = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Value'))

    class Meta:
        verbose_name_plural = 'Other Salaries'
        unique_together = ('employee_contract', 'salary_name')
