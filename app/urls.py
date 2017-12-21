from django.urls import path, include
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('user/logout/', auth_views.logout, {'template_name': 'app/home.html'}, name='logout'),
    #login and other user auth views provided by django built-in module
    path('user/', include('django.contrib.auth.urls')),
    path('logtime/', views.logTime, name='log-time'),   
    path('view-times/', views.viewMyTimes, name='view-my-times'),
    path('edit-time/([0-9]+)/', views.editTime, name='edit-time'),
    path('delete-time/([0-9]+)/', views.deleteTime, name='delete-time'),
    path('projects-view/', views.projectsView, name='projects-view'),
    path('users-view/', views.usersView, name='users-view'),
    path('get-project-csv/', views.getProjectCSV, name='get-project-csv'),
    path('signup/', views.createAccount, name='create-account'),
]
