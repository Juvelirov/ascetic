from django.db import models
import uuid
from study_project.models import Person, Class


class Project(models.Model):
    owner = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="project_img", default="project_img/default")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ['-created']


