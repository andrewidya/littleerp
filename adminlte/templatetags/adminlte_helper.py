from django import template

register = template.Library()

@register.filter(name='bootstraped_column_from_length')
def bootstraped_column_from_length(value, column_size):
	return column_size / len(value)