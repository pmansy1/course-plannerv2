from django.core.management.base import BaseCommand
from pandas import read_csv as panda
from course_dive.models import Course
from course_dive.recomended_model.path_planner.preprocessing import (
    extract_keywords,
    extract_prerequisites,
    extract_level,
    extract_credit_hours
)

class Command(BaseCommand):
    help = 'Import courses from a CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_path']
        df = panda(csv_path)

        self.stdout.write(f"CSV Columns: {df.columns.tolist()}")

        count = 0
        Course.objects.all().delete()
        for _, row in df.iterrows():
            title = row.get('Course Title', '').strip()
            if not title:
                continue  # Skip rows without titles

            description = row.get('Description', '')
            credit_hours = extract_credit_hours(title)
            level = extract_level(description)
            keywords = extract_keywords(description)
            prerequisites = extract_prerequisites(description)

            course, created = Course.objects.get_or_create(
                title=title,
                defaults={
                    'description': description,
                    'credit_hours': credit_hours,
                    'level': level,
                    'keywords': keywords,
                    'instructor': 'TBD',
                }
            )

            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} new courses.'))