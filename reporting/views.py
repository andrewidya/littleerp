from reporting.response import PDFResponse

from django.views.generic.base import TemplateResponseMixin, TemplateView


class PDFTemplateResponseMixin(TemplateResponseMixin):
    response_class = PDFResponse
    filename = None
    content_type = 'application/pdf'

    def get_filename(self):
        return self.filename

    def render_to_response(self, *args, **kwargs):
        kwargs['filename'] = self.get_filename()
        return super(PDFTemplateResponseMixin, self).render_to_response(*args, **kwargs)


class PDFTemplateView(TemplateView, TemplateResponseMixin):
    pass



