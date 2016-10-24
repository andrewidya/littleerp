#!/usr/bin/env python
import argparse

from django_reporting.utils import Reporting
from django.template import Template, Context
from django.conf import settings

from z3c.rml import rml2pdf

def render(template_file, output_file):
	settings.configure()
	template = Template(open(template_file).read())
	rml = template.render(Context({}))
	rml.encode('utf-8')
	data = rml2pdf.parseString(rml)

	with open(output_file, 'w') as output:
		output.write(data.read())

def main():	
	parser = argparse.ArgumentParser(description='render rml file template into pdf, contoh: ./pdfrender.py template.rml -o output.pdf')
	parser.add_argument('template', help='file template format *.rml sing bakal di convert dadi pdf')
	parser.add_argument('-o', '--output', help='jeneng file output pdf e john, misal file.pdf')
	args = parser.parse_args()
	if args.output and args.template:
		render(args.template, args.output)

if __name__ == "__main__":
	main()
	