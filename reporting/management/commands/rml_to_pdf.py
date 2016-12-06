from django.core.management.base import BaseCommand
from django.template import Template, Context

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			'template',
			help='file template with *.rml format to convert into pdf')
		parser.add_argument(
			'-o',
			'--output',
			help='pdf output file name of rendered pdf')

	def handle(self, *args, **options):
		from z3c.rml import rml2pdf

		template_file = options['template']
		output_file = ''
		if options['output']:
			output_file = options['output']
		elif options['o']:
			output = options['o']

		template = Template(open(template_file).read())
		rml = template.render(Context({}))
		rml.encode('utf-8')
		data = rml2pdf.parseString(rml)

		with open(output_file, 'w') as output:
			output.write(data.read())