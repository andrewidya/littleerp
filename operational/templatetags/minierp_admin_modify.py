from django import template
from fsm_admin.templatetags.fsm_admin import fsm_submit_row
from django.conf import settings
register = template.Library()


FSM_SUBMIT_BUTTON_TEMPLATE = 'fsm_admin/fsm_submit_button.html'
FSM_SUBMIT_LINE_TEMPLATE = 'fsm_admin/fsm_submit_line.html'
if 'grappelli' in settings.INSTALLED_APPS:
    FSM_SUBMIT_BUTTON_TEMPLATE = 'fsm_admin/fsm_submit_button_grappelli.html'
    FSM_SUBMIT_LINE_TEMPLATE = 'fsm_admin/fsm_submit_line_grappelli.html'
if 'suit' in settings.INSTALLED_APPS:
    FSM_SUBMIT_BUTTON_TEMPLATE = 'fsm_admin/fsm_submit_button_suit.html'
    FSM_SUBMIT_LINE_TEMPLATE = 'fsm_admin/fsm_submit_line_suit.html'
if 'wpadmin' in settings.INSTALLED_APPS:
    FSM_SUBMIT_BUTTON_TEMPLATE = 'fsm_admin/fsm_submit_button_wpadmin.html'
    FSM_SUBMIT_LINE_TEMPLATE = 'fsm_admin/fsm_submit_line_wpadmin.html'

@register.inclusion_tag(FSM_SUBMIT_LINE_TEMPLATE, takes_context=True)
def minierp_submit_row_without_save_button(context):
	ctx = fsm_submit_row(context)
	ctx['show_save'] = False
	ctx['show_save_as_new'] = False
	ctx['show_save_and_continue'] = False
	ctx['show_save_and_add_another'] = False
	return ctx
