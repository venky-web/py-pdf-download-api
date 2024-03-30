from rest_framework.response import Response
from rest_framework.decorators import api_view
import pdfkit
from django.http import HttpResponse

import PyPDF2, io
from PyPDF2 import PdfReader

from api.models import Report

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

options = {
    'page-size': 'A4',
    'margin-top': '2in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    # 'encoding': "UTF-8",
    # 'custom-header': [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'cookie': [
    #     # ('cookie-empty-value', '""')
    #     ('cookie-name1', 'cookie-value1'),
    #     ('cookie-name2', 'cookie-value2'),
    # ],
    # 'no-outline': None,
    'enable-local-file-access': None
}

@api_view(['GET'])
def getData(request):
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sample HTML</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a sample HTML file.</p>
        </body>
        </html>
        """
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html_content, 'report.pdf', configuration=config, options=options)

    if pdf:
        with open('report.pdf', 'rb') as report:
            file = report.read()

            response = HttpResponse(file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="pdf_content.pdf"'
            return response
    response = Response({'name': 'venky-web'})
    return response


@api_view(['DELETE'])
def DeleteReports(self):
    Report.objects.all().delete()
    return Response({'delete': 'successful'})
