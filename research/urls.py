from django.urls import path
from . import views

app_name = 'research'

urlpatterns = [
    path('research/publications/', views.publications_list,name='publications_list'),
    path('research/publications/<int:id>/', views.publication_detail, name='publication_detail'),
    path('research/focus/', views.focus, name='focus'),
    path('research/', views.index, name='index'),
    path('research/resource', views.resource, name='resource'),
]