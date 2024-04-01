from rest_framework.response import Response
from rest_framework.decorators import api_view
import pdfkit
import json
from django.http import HttpResponse

from api import serializers, models
from api.helper_functions import get_widgets_from_page
from api.pdf_functions import append_generated_html

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        # ('cookie-empty-value', '""')
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None,
    'enable-local-file-access': None,
    'user-style-sheet': 'style.css'
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
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a sample HTML file.</p>
        </body>
        </html>
        """
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    html_content = append_generated_html('report.html', '<!-- append_here -->')
    pdf = pdfkit.from_string(html_content, 'report.pdf', configuration=config, options=options)
    # pdf = pdfkit.from_file('report.html', 'report.pdf', configuration=config, options=options)

    if pdf:
        with open('report.pdf', 'rb') as report:
            file = report.read()

            response = HttpResponse(file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            return response
    response = Response({'name': 'venky-web'})
    return response


@api_view(['DELETE'])
def DeleteReports(self):
    models.Report.objects.all().delete()
    return Response({'delete': 'successful'})

@api_view(['DELETE'])
def DeletePages(self):
    models.Report_Page.objects.all().delete()
    return Response({'delete': 'successful'})

@api_view(['DELETE'])
def DeleteFeaturePages(self):
    models.Report_Feature_Page.objects.all().delete()
    return Response({'delete': 'successful'})


@api_view(['GET'])
def get_report(request):
    report_id = request.query_params.get('report_id')

    # Check if report_id parameter is provided in the request
    if report_id is None:
        return Response({'error': 'Report ID parameter is missing'}, status=400)

    # Query the database to get the report based on report_id
    try:
        report = models.Report.objects.get(report_id=report_id)
        pages = models.Report_Page.objects.filter(report_id=report_id)
    except models.Report.DoesNotExist:
        return Response({'error': 'Report not found'}, status=404)

    # Serialize the report data
    serializer = serializers.ReportSerializer(report)
    response_data = serializer.data
    response_data['pages'] = serializers.PageSerializer(pages, many=True).data

    # Return the report data as JSON response
    return Response(response_data)


@api_view(['GET'])
def get_page(request):
    page_id = request.query_params.get('page_id')

    # Check if page_id parameter is provided in the request
    if page_id is None:
        return Response({'error': 'Page ID parameter is missing'}, status=400)

    # Query the database to get the report based on page_id
    try:
        page = models.Report_Page.objects.get(page_id=page_id)
        # widgets = models.Widget.objects.filter(page_id=page_id)
        print(get_widgets_from_page(page))

    except models.Report_Page.DoesNotExist:
        return Response({'error': 'Page not found'}, status=404)

    # Serialize the report data
    serializer = serializers.PageSerializer(page)
    response_data = serializer.data
    # response_data['widgets'] = serializers.WidgetSerializer(widgets, many=True).data

    # Return the report data as JSON response
    return Response(response_data)