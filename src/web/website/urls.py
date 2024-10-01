from django.urls import path
from .views import team_view
from .views import blog_view
from .views import project_view
from .views import contact_view
from .views import about_view
from .views import service_view
from .views import service_details_view
from django.urls import path
from .views import blog_details_view
from .views import project_details_view

from .views import (
    HomeView
)

app_name = "website"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team/', team_view, name='team'),
    path('blog/', blog_view, name='blog'),
    path('project/', project_view, name='project'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('service/', service_view, name='service'),
    path('service-details/', service_details_view, name='service-details'),
    path('blog-details/', blog_details_view, name='blog-details'),
    path('project-details/', project_details_view, name='project-details'),


    ]


