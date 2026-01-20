# api/urls.py
from django.urls import path
from apiapp import views
from .views import receive_xml

urlpatterns = [
    path('receive/', views.receive_xml, name='submit_xml'),
]
