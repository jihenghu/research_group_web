from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('contactus/', views.contactus,name='contactus'),
    path('submit_message/', views.submit_message,name='submit_message'),
]