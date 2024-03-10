from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from management.models import Patientinfo
from .models import Bill
from django.http import JsonResponse


# Create your views here.
def bill_count(request):
    patient_info = Patientinfo.objects.all()
    return render(request, 'bill/bill_form.html', {'patient_info':patient_info})
    # return HttpResponse("hello")
    # return redirect('view-bill')
    # return reve

def submit_bill(request):
    doc_cahrge = int(request.POST.get('dc'))
    rc = int(request.POST.get('rc'))
    day = int(request.POST.get('day'))
    total = rc + doc_cahrge
    patient_id = Patientinfo.objects.get(id=int(request.POST.get('patient')))
    bill = Bill(patient_id=patient_id, doctor_charge=doc_cahrge, room_charge=rc, no_of_days=day,total=total)
    bill.save()
    print("\n\nrecord", doc_cahrge,patient_id, total)
    responce = JsonResponse({"hello":"hello"})
    return responce


