from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200 , unique=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag , related_name="tags_project")


    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images_project" , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images/")


    def __str__(self):
        return f"{self.Project.title} Image "