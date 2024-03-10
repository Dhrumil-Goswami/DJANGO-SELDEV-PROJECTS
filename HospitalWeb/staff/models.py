from django.db import models


# Create your models here.
class Staff(models.Model):
    doctor_name = models.CharField(max_length=455)
    treatment_type = [
        ('hear', 'Hear'),
        ('ortho', 'Ortho'),
        ('bodycheckup', 'Bodycheckup'),
    ]
    type_treatment = models.CharField(
        max_length=11,
        choices=treatment_type,
        default='Hear',
    )
    doc_pic = models.ImageField(upload_to='media/', default='media/un.jpg')

    def __str__(self):
        return self.doctor_name
