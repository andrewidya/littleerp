from django.template import Template, Context
from django.http import HttpResponse
from cStringIO import StringIO
from z3c.rml import rml2pdf

class Reporting(object):
	def __init__(self, context, template_name=None, output=None):
		if template_name is None:
			raise "template_name parameter must be not None"
		self.template_name = template_name
		if isinstance(context, Context):
			self.context = context
		else:
			raise "context parameter must be instance of Context class"
		if output is not None:
			self.output_file = output
		else:
			self.output_file = "default.pdf"

	def get_template(self):
		template = Template(open(self.template_name).read())
		return template

	def get_context_data(self):
		return self.context

	def render(self):
		template = self.get_template()
		rml = template.render(self.get_context_data())
		#rml.encode('utf-8')
		#buf = StringIO()
		data = rml2pdf.parseString(rml)
		#buf.reset()
		#pdf_data = buf.read()
		response = HttpResponse(content_type='application/pdf')
		response.write(data.read())
		response['Content-Disposition'] = 'attachment; filename="default.pdf"'
		return response

