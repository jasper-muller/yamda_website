from django.db import models
from django.conf.urls.static import static


# Create your models here.

class HeadlineSection(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class WorkSection(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(null=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class ContactSection(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
