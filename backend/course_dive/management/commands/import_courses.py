from django.core.management.base import BaseCommand
import pandas as pd
from course_dive.models import Course, Prerequisite
from course_dive.recomended_model.path_planner.preprocessing import clean_code

class Command(BaseCommand):
    help = 'Import courses from the cleaned and structured CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_path']
        df = pd.read_csv(csv_path)
        df.fillna('', inplace=True)

        self.stdout.write(f"Loaded CSV with {len(df)} rows.")

        Course.objects.all().delete()  # clear previous records

        # 📝 First pass: create all courses without prerequisites
        for _, row in df.iterrows():
            title = row['Course Title'].strip()
            if not title:
                continue

            Course.objects.create(
                title=title,
                description=row['Description'] or "No description provided.",
                credit_hours=int(row['credit_hours']) if row['credit_hours'] else 0,
                level=row['level'] or "Unknown",
                keywords=row['keywords'] or "No keywords",
                department=row['Course'] or "Other",
                crn=int(row['n']) if 'n' in row and not pd.isna(row['n']) else 0
            )

        # 📝 Second pass: add prerequisites and notes
        for _, row in df.iterrows():
            title = row['Course Title'].strip()
            course = Course.objects.get(title=title)

            # Handle prerequisites (course codes)
            prereq_str = row['prerequisites']
            if prereq_str:
                prereq_codes = [clean_code(p) for p in prereq_str.split(",") if p.strip()]
                for code in prereq_codes:
                    prereq_course = Course.objects.filter(title__icontains=code).first()
                    if prereq_course:
                        Prerequisite.objects.create(course=course, prerequisite_course=prereq_course)
                    else:
                        # Save as note if course code not found (edge case fallback)
                        Prerequisite.objects.create(course=course, note=code)
                        self.stdout.write(f"⚠️ Prerequisite course not found for '{title}', saved as note: '{code}'")

            # Handle prereq notes (non-course requirements)
            prereq_notes = row.get('prereq_notes', '')
            if prereq_notes:
                notes_list = [n.strip() for n in prereq_notes.split(",") if n.strip()]
                for note in notes_list:
                    Prerequisite.objects.create(course=course, note=note)

        self.stdout.write(self.style.SUCCESS('✅ Successfully imported courses with prerequisites and notes.'))