"""
    Command to import data from csv file and save to DB
"""

import csv
from django.core.management.base import BaseCommand

from api.models import Page_Widget_Mapping

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
                model_Instance = Page_Widget_Mapping(
                    mapping_id = row['mapping_id'],
                    page_id = row['page_id'],
                    widget_id = row['widget_id'],
                    page_type = row['page_type'],
                )
                # Save the instance to the database
                model_Instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
