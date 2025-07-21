from django.apps import AppConfig


class CourseDiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_dive'

def ready(self):
    import course_dive.signals