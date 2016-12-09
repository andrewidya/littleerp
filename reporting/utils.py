from z3c.rml import rml2pdf
from weasyprint import HTML

from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


class RML2PDF(object):
    template_name = None
    context = None

    def __init__(self, context, template_name=None, output=None):
        if template_name is not None:
            self.template_name = template_name
        if self.template_name is None:
            raise "template_name parameter must be not None"

        if isinstance(context, Context):
            self.context = context
        else:
            raise "context parameter must be instance of Context class"

        if output is None:
            self.output_file = "default.pdf"
        else:
            self.output_file = output

    def get_template(self):
        # template = Template(open(self.template_name).read())
        template = get_template(self.template_name)
        return template

    def get_context_data(self):
        context = self.context
        context['filename'] = self.output_file
        return context

    def render(self):
        template = self.get_template()
        rml = template.render(self.get_context_data())
        rml.encode('utf-8')
        data = rml2pdf.parseString(rml)
        response = HttpResponse(content_type='application/pdf')
        response.write(data.read())
        response[
            'Content-Disposition'] = 'filename="{0}"'.format(self.output_file)
        return response


class HTML2PDF(object):
    template_name = None
    context = None

    def __init__(self, context, template_name=None, output=None):
        if template_name is not None:
            self.template_name = template_name
        if self.template_name is None:
            raise "template_name parameter must be not None"

        if isinstance(context, Context):
            self.context = context
        else:
            raise "context parameter must be instance of Context class"

        if output is None:
            self.output_file = "default.pdf"
        else:
            self.output_file = output

    def get_template(self):
        # template = Template(open(self.template_name).read())
        template = get_template(self.template_name)
        return template

    def get_context_data(self):
        context = self.context
        context['filename'] = self.output_file
        return context

    def get_output_file(self):
        return self.output_file

    def render(self, request):
        template = self.get_template()
        html_string = template.render(self.get_context_data()).encode('utf-8')

        # pdf_data = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{0}"'.format(self.output_file)

        HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(response)

        return response
