from django.urls import path
from . import views

urlpatterns = [
path('view-task', views.view_task),
path('create-task', views.create_task),
path('delete-task/<str:pk>/', views.delete_task),
]