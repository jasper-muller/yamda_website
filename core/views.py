from django.shortcuts import render

from .models import HeadlineSection, WorkSection, Project, AboutSection, ContactSection

# Create your views here.
def main(request):

    all_projects = Project.objects.all()

    visible_projects = [project for project in all_projects if project.visible]

    context = {
        'headline_section': HeadlineSection.objects.first(),
        'work_section': WorkSection.objects.first(),
        'project_list': visible_projects,
        'project_slide_number': range(len(visible_projects)),
        'about_section': AboutSection.objects.first(),
        'contact_section': ContactSection.objects.first()
    }
    return render(request, 'core/main.html', context)
