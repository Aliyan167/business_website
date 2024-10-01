from django.urls import path
from .views import TeamMemberListView, TeamMemberDetailView



urlpatterns = [
    path('member/', TeamMemberListView.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamMemberDetailView.as_view(), name='team-member-detail'),
]
