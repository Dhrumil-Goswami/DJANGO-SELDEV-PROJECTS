from django.contrib import admin
from .models import Bill


# Register your models here.
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['total', 'patient_id', 'no_of_days']
