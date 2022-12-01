from django.urls import path
from . import views


urlpatterns = [
    path('', views.search),
    path("asn", views.get_asn)
]