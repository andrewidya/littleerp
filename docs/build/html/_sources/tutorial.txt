========
Tutorial
========

Adding Report Button on Admin Change Form
=========================================

We provide 2 Mixin to be integrated into django admin in order
to generate pdf report generation. You can choose one of this Mixin:

1. HTMLModelReportMixin
2. RMLModelReportMixin
   
The different between these 2 mixin just in the engine used in generation process, ``HTMLModelReportMixin`` use WeasyPrint to render
html template into pdf report and ``RMLModelReportMixin`` use ReportLab
to render rml template into pdf.

To use this mixins, simply just by inherit from this mixin before default django model admin class and set ``report_template`` with your
template

It's easy to explain with examples::

	from django_reporting.admin import HTMLModelReportMixin
	from django.contrib import admin
	from my_apps.models import SomeModel

	@admin.register(SomeModel)
	class SomeModelAdmin(HTMLModelReportMixin, admin.ModelAdmin):
		report_template = 'my_apps/templates/report_templates.html'


Using Utils to Generate PDF Report
==================================

We provide two to helper in ``django_reporting.utils`` module
to generate pdf report, you can choose ``RML2PDF`` class or
``HTML2PDF`` class to generate report and layouting using
appropriate mark up languate. These classes shared similar api call, see also utils api documentation

a brief example how to generate pdf report from custom view::

   from django.template import Context   
   from django_reporting.utils import HTML2PDF
   from hrm.models import Employee

   def employee_list_view(request):
      employee = Employee.objects.all()
      context = Context({'objects': employee})
      pdf = HRML2PDF(context, template_name='hrm/templates/employee.html', output='employee_list.pdf')
      return = html_pdf.render(request)




