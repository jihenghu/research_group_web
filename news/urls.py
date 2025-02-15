from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.list,name='list'),
    path('news/<int:id>/', views.detail, name='detail'),
]