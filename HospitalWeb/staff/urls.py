from django.http import request
from django.urls import path
from . import views
# TemplateView.as_view(template_name='staff.html')
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from management.forms import StaffForm
app_name = 'staff'

urlpatterns = [
    path('', views.add_staff, name='add-staff'),
    path('add', views.save_staff, name='staff-page'),
    path('/staff/view', views.view_staff, name='staff-view'),
]
