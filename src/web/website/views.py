from django.shortcuts import render
from django.views.generic import TemplateView
from .blogs.models import BlogPost

# Create your views here.
class HomeView(TemplateView):
    template_name = 'website/index.html'


def team_view(request):
    return render(request, 'website/team.html')


from django.core.paginator import Paginator

def blog_view(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 4)  # Adjust number of posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'website/blog.html', {'posts': page_obj})  # Use page_obj for pagination




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


