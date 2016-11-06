from functools import update_wrapper

from django.core.exceptions import ImproperlyConfigured
from django.template import Context
from django.contrib.admin.utils import unquote

class BaseReport(object):
    def get_model_info(self):
        app_label = self.model._meta.app_label
        try:
            return (app_label, self.model._meta.model_name,)
        except AttributeError:
            return (app_label, self.model._meta.module_name,)

class ModelDetailReportMixin(BaseReport):
    report_template = None
    report_context_object_name = None
    report_output = None

    change_form_template = "admin/django_reporting/change_form_report.html"

    def get_urls(self):
        """
        Get default django admin urls then add custom url for report link
        """
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view, cacheable=True)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.get_model_info()
        urls = super(ModelDetailReportMixin, self).get_urls()
        report_url = [
            url(r'^(.+)/report/$', wrap(self.report), name='%s_%s_report' % info),
        ]

        return report_url + urls

    def get_context_object_name(self):
        """
        Get the name to use for object in template
        """
        if self.report_context_object_name:
            return self.report_context_object_name
        return None

    def get_context_data(self, obj):
        """
        Insert singgle object into context dict
        """
        if self.report_context_object_name:
            context = Context({
                self.report_context_object_name: obj
                })
        else:
            context = Context({'object': obj})
        return context

    def get_report_template(self):
        if self.report_template:
            return self.report_template
        else:
            raise ImproperlyConfigured(
                "{0} attribute value is {1}, {2}'s report_template is missing".format(
                    "report_template", self.report_template, self.__class__.__name__)
                )

    def get_output_filename(self):
        if self.report_output is None:
            return "default.pdf"
        return self.report_output

    def report(self, request, object_id, extra_context=None):
        from .utils import Reporting

        obj = self.get_object(request, unquote(object_id))

        template = self.get_report_template()
        output_file = self.get_output_filename()
        context = self.get_context_data(obj)

        report = Reporting(context, template_name=template, output=output_file)
        return report.render()

class HTMLModelReportMixin(BaseReport):
    report_template = None
    report_context_object_name = None
    report_output = None

    change_form_template = "admin/django_reporting/change_form_report.html"

    def get_urls(self):
        """
        Get default django admin urls then add custom url for report link
        """
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view, cacheable=True)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.get_model_info()
        urls = super(HTMLModelReportMixin, self).get_urls()
        report_url = [
            url(r'^(.+)/report/$', wrap(self.report), name='%s_%s_report' % info),
        ]

        return report_url + urls

    def get_context_object_name(self):
        """
        Get the name to use for object in template
        """
        if self.report_context_object_name:
            return self.report_context_object_name
        return None

    def get_context_data(self, obj):
        """
        Insert singgle object into context dict
        """
        if self.report_context_object_name:
            context = Context({
                self.report_context_object_name: obj
                })
        else:
            context = Context({'object': obj})
        return context

    def get_report_template(self):
        if self.report_template:
            return self.report_template
        else:
            raise ImproperlyConfigured(
                "{0} attribute value is {1}, {2}'s report_template is missing".format(
                    "report_template", self.report_template, self.__class__.__name__)
                )

    def get_output_filename(self):
        if self.report_output is None:
            return "default.pdf"
        return self.report_output

    def report(self, request, object_id, extra_context=None):
        from .utils import HTML2PDF

        obj = self.get_object(request, unquote(object_id))

        template = self.get_report_template()
        output_file = self.get_output_filename()
        context = self.get_context_data(obj)

        report = HTML2PDF(context, template_name=template, output=output_file)
        return report.render()