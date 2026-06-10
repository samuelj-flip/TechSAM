from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("status/", views.hunter_status_view, name="hunter_status"),
]
