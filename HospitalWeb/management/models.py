from django.db import models
from staff.models import Staff


# Create your models here.
class Patientinfo(models.Model):
    f_name = models.CharField(max_length=150)
    l_name = models.CharField(max_length=150)
    un_name = models.CharField(max_length=150)
    pwd = models.CharField(max_length=150)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
