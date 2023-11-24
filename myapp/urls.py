from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('create-tasks/', views.create_task, name='create-tasks'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('create-project/', views.create_project, name='create-project'),
    path('projects/<slug:project_slug>/edit/', views.edit_project, name='edit_project'),
    path('projects/<str:project_slug>/virtual-tour/', views.virtual_tour, name='virtual_tour'),
     path('upload/', views.upload_floorplan, name='upload_floorplan'),
    path('markers/', views.markers, name='markers'),

    path('projects/<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('virtual/', views.virtual_view, name='virtual'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dash, name='dashboard'),
    path('test/', views.test, name='test'),
]
