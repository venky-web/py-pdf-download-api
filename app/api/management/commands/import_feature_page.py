"""
    Command to import data from csv file and save to DB
"""

import csv
from datetime import datetime
from django.core.management.base import BaseCommand

from api.models import Report_Feature_Page

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
                model_Instance = Report_Feature_Page(
                    feature_page_id = row['feature_page_id'],
                    object_id = row['object_id'],
                    object_type = row['object_type'],
                    definition = row['definition'],
                )
                try:
                    model_Instance.container_id = int(row['container_id'])
                except:
                    model_Instance.container_id = 81
                    print(f"Error: {row['object_type']} create by or update by error.")

                try:
                    model_Instance.created_by = int(row['created_by'])
                except:
                    print(f"Error: {row['object_type']} create by or update by error.")

                try:
                    model_Instance.updated_by = int(row['updated_by'])
                except:
                    print(f"Error: {row['object_type']} create by or update by error.")
                    
                try:
                    model_Instance.created_date = datetime.strptime(row['created_date'], '%Y-%m-%d %H:%M:%S.%f')
                except:
                    print(f"Error: {row['object_type']} create by or update by error.")

                try:
                    model_Instance.updated_date = datetime.strptime(row['updated_date'], '%Y-%m-%d %H:%M:%S.%f')
                except:
                    print(f"Error: {row['object_type']} create by or update by error.")
                # Save the instance to the database
                model_Instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
