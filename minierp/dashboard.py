"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'minierp.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    template = 'grappelli/dashboard/dashboard.html'
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('HRM Applications'),
            column = 1,
            collapsible = True,
            children = [
                modules.ModelList(
                    _('Employee & Contract'),
                    column = 1,
                    collapsible = True,
                    models = ('hrm.models.Employee',
                        'hrm.models.EmployeeContract',
                        'hrm.models.JobTitle',
                        'hrm.models.Division',
                    )
                ),
                modules.ModelList(
                    _('Leaves & Education'),
                    column = 1,
                    collapsible = True,
                    models = ('hrm.models.LeaveType',
                        'hrm.models.AnnualLeave',
                        'hrm.models.LeaveTaken',
                        'hrm.models.Education',
                    )
                ),
                modules.ModelList(
                    _('Periodic Evaluation'),
                    column = 1,
                    collapsible = True,
                    models = ('hrm.models.EvaluationPeriod',
                        'hrm.models.EvaluationItem',
                        'hrm.models.Evaluation',
                        'hrm.models.EvaluationDetail',
                    )
                ),
                modules.ModelList(
                    _('Salary Information'),
                    column = 1,
                    collapsible = True,
                    models = ('hrm.models.SalaryCategory',
                        'hrm.models.SalaryName',
                        'hrm.models.OtherSalary',
                    )
                ),
                modules.ModelList(
                    _('Performance & Evaluation'),
                    column = 1,
                    collapsible = True,
                    models = ('hrm.models.Evaluation',
                        'hrm.models.EvaluationPeriod',
                        'hrm.models.EvaluationItem',
                    )
                ),
                modules.ModelList(
                    _('Others Information'),
                    column = 1,
                    collapsible = True,
                    models = ('hrm.models.BankName',)
                ),
            ]
        ))

        self.children.append(modules.Group(
            _('CRM Applications'),
            column = 2,
            collapsible = True,
            children = [
                modules.ModelList(
                    _('Customer Information & Service Provided'),
                    column = 1,
                    collapsible = True,
                    models = ('crm.models.Customer',
                        'crm.models.Service',
                    )
                ),
                modules.ModelList(
                    _('Sales Order & Details'),
                    column = 1,
                    collapsible = True,
                    models = ('crm.models.SalesOrder',
                        'crm.models.SalesOrderDetail',
                        'crm.models.ItemCategory',
                        'crm.models.ServiceSalaryItem',
                        'crm.models.ServiceSalaryDetail',
                    )
                ),
                modules.ModelList(
                    _('Customer Satisfication & Interview'),
                    column = 1,
                    collapsible = True,
                    models = ('crm.models.Satisfication',
                        'crm.models.SatisficationDetail',
                        'crm.models.SatisficationPointRateItem',
                        'crm.models.SatisficationPointCategory',
                    )
                ),
            ]
        ))

        self.children.append(modules.Group(
            _('Operational Applications'),
            column = 2,
            collapsible = True,
            children = [
                modules.ModelList(
                    _('Visit Customer Activity'),
                    column = 1,
                    collapsible = True,
                    models = ('operational.models.VisitCustomer',
                        'operational.models.VisitPointRateItem',
                    )
                ),
                modules.ModelList(
                    _('Payroll'),
                    column = 1,
                    collapsible = True,
                    models = ('operational.models.PayrollPeriod',
                        'operational.models.Payroll',
                        'operational.models.PayrollDetail',
                    )
                )
            ],
        ))

        self.children.append(modules.Group(
            _('Finance Applications'),
            column = 2,
            collapsible = True,
            children = [
                modules.ModelList(
                    _('Payroll Expense'),
                    column = 1,
                    collapsible = True,
                    models = ('finance.models.PaidPayroll',)
                )
            ],
        ))

        """
        self.children.append(modules.Group(
            _('Group: Administration & Applications'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=3,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Applications'),
                    column=2,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                )
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('AppList: Applications'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('ModelList: Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))
        """
        self.children.append(modules.AppList(
            title='Administration',
            column=3,
            models=('django.contrib.*',)
        ))
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=3,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        """
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))

        # append a feed module
        self.children.append(modules.Feed(
            _('Latest Django News'),
            column=2,
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))
        """

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=4,
        ))



