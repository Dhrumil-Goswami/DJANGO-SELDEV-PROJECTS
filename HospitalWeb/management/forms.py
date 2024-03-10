from django import forms
from django.forms import ModelForm
from .models import Patientinfo
from staff.models import Staff


class PatientForm(ModelForm):
    class Meta:
        model = Patientinfo
        fields = ('f_name', 'l_name', 'un_name', 'pwd', 'staff_id')
        # labels ={
        #     'f_name':'',
        #     'l_name':''
        # }
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control'}),
            'un_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pwd': forms.TextInput(attrs={'class': 'form-control'}),
            'staff_id': forms.Select(attrs={'class': 'form-control'}),
        }


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ('doctor_name', 'type_treatment')
        widgets = {
            'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type_treatment': forms.Select(attrs={'class': 'form-control'}),
        }
