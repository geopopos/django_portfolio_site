from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    project_link = models.URLField(default="#")

    def images(self):
        return Image.objects.filter(project=self).order_by('order')

    def header_image(self):
        return Image.objects.filter(project=self).filter(order=0)

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.FilePathField(path="/img")
    order = models.IntegerField(default=0)
