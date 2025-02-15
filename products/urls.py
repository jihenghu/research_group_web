from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products,name='products'),
    path('products/<slug>', views.detail,name='detail'),
    path('products/access/<slug>', views.access,name='access'),
    path('products/document/<slug>', views.document,name='document'),
    path('batch_upload/', views.batch_upload,name='batch_upload'),
    path('productimages/', views.product_images,name='product_images'),
    path('ajaxpic/', views.ajaxpic,name='ajaxpic'),
]