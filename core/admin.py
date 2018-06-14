from django.contrib import admin
from .models import HeadlineSection, AboutSection, ContactSection, WorkSection, Project

# Register your models here.
admin.site.register(HeadlineSection)
admin.site.register(AboutSection)
admin.site.register(ContactSection)
admin.site.register(WorkSection)
admin.site.register(Project)
