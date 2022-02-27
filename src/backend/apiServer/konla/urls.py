from django.urls import path,include
from . import views

urlpatterns = [
    path("upload/binary",views.uploadFile,name="acceptFile"),
    path("upload/url",views.uploadURL,name="acceptURL"),
    path("upload/start",views.uploadStart,name="startProcessing"),
    path("keywords",views.keywords,name="keywords"),
]