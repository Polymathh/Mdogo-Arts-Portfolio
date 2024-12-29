from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cartoon/<int:pk>/', views.cartoon_detail, name='cartoon_detail'),
    
]