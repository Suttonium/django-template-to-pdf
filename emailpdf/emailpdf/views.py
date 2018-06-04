from django.views.generic import View
from .utils import *


class GeneratePDF(View):
    template_name = "emailpdf/invoice.html"

    def get(self, request, *args, **kwargs):
        context = {
            'invoice_id': 123,
            'customer_name': 'Austin Sutton',
            'amount': 1399.99,
            'today': "Today"
        }
        pdf = render_to_pdf(self.template_name, context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "invoice_{}.pdf".format(context['invoice_id'])
            # content = "inline; filename={}".format(filename)
            content = "attachment; filename={}".format(filename)
            # download = request.GET.get("download")
            # if download:
            #     content = "attachment; filename={}".format(filename)

            response['Content-Disposition'] = content
            return response
        return HttpResponse('Not Found')
