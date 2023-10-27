from django.apps import AppConfig


class StudyProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'study_project'

    def ready(self):
        import study_project.signals