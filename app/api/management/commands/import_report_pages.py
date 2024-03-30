"""
    Command to import data from csv file and save to DB
"""

import csv
from datetime import datetime
from django.core.management.base import BaseCommand

from api.models import Report_Page

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        # Open the CSV file and read its contents
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create an instance of the model and populate its fields
                model_Instance = Report_Page(
                    report_id = row['report_id'],
                    page_id = row['page_id'],
                    page_name = row['page_name'],
                    definition = row['definition'],
                    status = row['status'],
                )
                try:
                    model_Instance.page_order = int(row['page_order'])
                except:
                    model_Instance.page_order = 0
                    print(f"Error: {row['page_name']} create by or update by error.")

                try:
                    model_Instance.created_by = int(row['created_by'])
                except:
                    print(f"Error: {row['page_name']} create by or update by error.")

                try:
                    model_Instance.updated_by = int(row['updated_by'])
                except:
                    print(f"Error: {row['page_name']} create by or update by error.")
                    
                try:
                    model_Instance.created_dt = datetime.strptime(row['created_dt'], '%Y-%m-%d %H:%M:%S.%f')
                except:
                    print(f"Error: {row['page_name']} create by or update by error.")

                try:
                    model_Instance.update_dt = datetime.strptime(row['update_dt'], '%Y-%m-%d %H:%M:%S.%f')
                except:
                    print(f"Error: {row['page_name']} create by or update by error.")
                # Save the instance to the database
                model_Instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
