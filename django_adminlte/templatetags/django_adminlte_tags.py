from django import template

from django_adminlte.settings import ADMIN_TITLE

register = template.Library()

@register.simple_tag
def get_admin_title():
	"""
	Return the title of admin interface
	"""
	return ADMIN_TITLE