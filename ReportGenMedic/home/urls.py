from django.urls import path
from . import views

urlpatterns = [
    path("patients/",views.patient_list,name="Patient-list"),
    path("patients/<str:name>/",views.patient_search,name="Search patient"),
    path("upload/",views.upload_image,name="upload x-ray"),
]