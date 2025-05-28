from django.core.management.base import BaseCommand
from course_dive.models import Course
from course_dive.recomended_model.path_planner.preprocessing import load_courses, extract_keywords, extract_prerequisites, extract_level, extract_credit_hours

class Command(BaseCommand):
    help = 'Import courses from CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_path']
        df = load_courses(csv_path)
        print("CSV Columns:", df.columns.tolist())

        count = 0
        for _, row in df.iterrows():
            title = row.get('Course Title', '').strip()
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
                }
            )

            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} new courses.'))