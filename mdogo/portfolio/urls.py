from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import logout_view


urlpatterns = [
    path('', views.home, name='home'),
    path('cartoon/<int:pk>/', views.cartoon_detail, name='cartoon_detail'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)