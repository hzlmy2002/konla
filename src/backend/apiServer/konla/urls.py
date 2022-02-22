from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("stat",views.stat),
    path("upload/binary",views.acceptFile,name="acceptFile"),
    path("upload/url",views.acceptURL,name="acceptURL"),
]