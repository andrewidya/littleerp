from weasyprint import HTML

from django.template.response import TemplateResponse
from django.template.context import _current_app_undefined
from django.conf import settings


class PDFResponse(TemplateResponse):
    def __init__(self, request, template, context=None, filename=None,
                 content_type='application/pdf', status=None,
                 current_app=_current_app_undefined, charset=None,
                 using=None):
        super(PDFResponse, self).__init__(request, template, context,
                                          content_type, status, current_app,
                                          charset, using)
        if filename:
            self['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
        else:
            self['Content-Disposition'] = 'attachment'

    @property
    def rendered_content(self):
        template = self._resolve_template(self.template_name)
        context = self._resolve_context(self.context_data)
        content = template.render(context, self._request).encode('utf-8')
        if hasattr(settings, 'WEASYPRINT_BASEURL'):
            base_url = settings.WEASYPRINT_BASEURL
        else:
            base_url = self._request.build_absolute_uri()
        return HTML(string=content, base_url=base_url).write_pdf()
