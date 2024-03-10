from django.urls import path
from . import views

app_name = 'bill'
urlpatterns = [
    path('charge', views.bill_count, name='view-bill'),
    path('sub', views.submit_bill, name='total-bill'),
]
