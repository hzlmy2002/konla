from django.urls import path
from . import views

urlpatterns = [
    path("upload/binary",views.uploadFile,name="acceptFile"),
    path("upload/url",views.uploadURL,name="acceptURL"),
    path("upload/start",views.uploadStart,name="startProcessing"),
    path("summarisation/whole",views.wholeSummarisation,name="provideWholeSummarisation"),
    path("summarisation/partial",views.partialSummarisation,name="providePartialSummarisation"),
    path("keywords",views.keywords,name="keywords"),
    path("info/refs",views.infoRefs,name="infoRefs"),
    path("info/metadata",views.infoMeta,name="infoMeta"),
    path("info/metrics",views.infoMetrics,name="infoMetrics"),
]