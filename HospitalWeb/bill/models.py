from django.db import models
from management.models import Patientinfo


# Create your models here.
class Bill(models.Model):
    patient_id = models.ForeignKey(Patientinfo, on_delete=models.CASCADE, null=True)
    doctor_charge = models.IntegerField()
    room_charge = models.IntegerField(default=350)
    no_of_days = models.IntegerField()
    total = models.FloatField()

