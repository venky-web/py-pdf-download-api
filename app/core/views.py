from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import pdfkit

class GeneratePDF(APIView):
    def post(self, request):
        # html_string = request.data.get('html_string', '')
        html_string = '<h1>Welcome to PDF Generator</h1>'

        # Generate PDF from HTML string
        pdf = pdfkit.from_string(html_string, False)

        # Return PDF as response
        response = Response(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'
        return response