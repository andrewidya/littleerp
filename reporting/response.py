from weasyprint import HTML

from django.http import HttpResponse
from django.template.response import TemplateResponse, ContentNotRenderedError
from django.template.context import _current_app_undefined


class PDFResponse(TemplateResponse):
    rendering_attrs = TemplateResponse.rendering_attrs + ['']

    def __init__(self, request, template, context=None,
                 content_type='application/pdf', status=None,
                 current_app=_current_app_undefined, charset=None,
                 using=None):
        super(PDFResponse, self).__init__(request, template, context,
                                          content_type, status, current_app,
                                          charset, using)

    @property
    def rendered_content(self):
        template = self._resolve_template(self.template_name)
        context = self._resolve_context(self.context_data)
        content = template.render(context, self._request).encode('utf-8')
        return HTML(string=content,
                    base_url=self._request.build_absolute_uri()).write_pdf()
