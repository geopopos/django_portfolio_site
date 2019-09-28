from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    project_link = models.URLField(default="#")
    image = models.FilePathField(path="/img")
