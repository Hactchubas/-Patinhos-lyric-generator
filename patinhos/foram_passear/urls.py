from django.urls import path
from . import views

app_name = "foram_passear"
urlpatterns = [
    path("",views.index, name="index"),
    path("letra", views.gerador, name="gerador")
]