from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='base'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('thankyou/', views.thankyou, name='thankyou'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)