from django.shortcuts import render
from django.views.generic import TemplateView

from src.apps.whisper.main import NotificationService


# Create your views here.
class HomeView(TemplateView):
    template_name = 'website/index.html'


def team_view(request):
    return render(request, 'website/team.html')


def blog_view(request):
    return render(request, 'website/blog.html')


def project_view(request):
    return render(request, 'website/project.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def about_view(request):
    return render(request, 'website/about.html')


def service_view(request):
    return render(request, 'website/service.html')


def service_details_view(request):
    return render(request, 'website/service-details.html')


def blog_details_view(request):
    return render(request, 'website/blog-details.html')


def project_details_view(request):
    return render(request, 'website/project-details.html')


