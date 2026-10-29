from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project, name='projects'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('leetcode/', views.leetcode, name='leetcode'),
    path('certificate/', views.certificate, name='certificate'),
    path('help/', views.help, name='help'),
    path("projects/remove/<int:project_id>/", views.remove_project,name="remove_project",),
]