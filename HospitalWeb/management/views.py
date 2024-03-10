from django.shortcuts import render, HttpResponse, redirect
from management.models import Patientinfo
from django.http import HttpResponseRedirect
from .forms import PatientForm
from staff.models import Staff


# Create your views here.
def index(request):
    return render(request, 'index.html')


def patientname(request):
    form = PatientForm(request.POST or None)
    staff = Staff.objects.all()
    return render(request, 'patient_form.html', {'staff': staff})


def patientinfo(request):
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    un_name = request.POST.get('un_name')
    pwd = request.POST.get('pwd')
    print("\n\nstaff", request.POST.get('staff'))
    staff_id = Staff.objects.get(id=int(request.POST.get('staff')))

    print("\n\nhdgfhds", f_name, pwd, staff_id)
    patientinfo = Patientinfo(f_name=f_name, l_name=l_name, un_name=un_name, pwd=pwd, staff_id=staff_id)
    print("\n\n", patientinfo)
    patientinfo.save()
    return render(request, 'index.html')


def patientdetails(request):
    patient_object = Patientinfo.objects.all()
    print("\n\nobject", patient_object)
    context = {'patients': patient_object}
    return render(request, 'views_record.html', context)


def delete_rec(request, id):
    # print("fffff", callback_kwargs, request.GET.get('id'))
    record = Patientinfo.objects.get(id=id)
    record.delete()
    # return render(request, 'index.html')
    return HttpResponseRedirect('/patientdetails')


def update_rec(request, id):
    record = Patientinfo.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('list-patient')
    context = {'record': record, 'form': form}
    return render(request, 'view_update.html', context)
