from django.contrib import admin
from django.urls import path
from management import views
urlpatterns = [
    path('', views.index, name='index'),
    path('patientform', views.patientname),
    path('patientinfo', views.patientinfo),
    path('patientdetails', views.patientdetails, name='list-patient'),
    path('delete_rec/<int:id>', views.delete_rec),
    path('update_rec/<int:id>', views.update_rec)
]