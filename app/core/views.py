from django.shortcuts import render

from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
import pdfkit

from core.auth import CsrfExemptSessionAuthentication

class GeneratePDF(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        # html_string = request.data.get('html_string', '')
        # html_string = '<h1>Welcome to PDF Generator</h1>'

        # Generate PDF from HTML string
        # pdf = pdfkit.from_string(html_string, 'report.pdf', options={"enable-local-file-access": ""})
        # pdf = pdfkit.from_url('http://google.com', 'report.pdf')
        html_file_path = "sample.html"
        pdf = pdfkit.from_file(html_file_path, "report.pdf")

        # Return PDF as response
        response = Response(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response
        # return Response({"message": "Api worked"})