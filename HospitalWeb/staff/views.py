from django.shortcuts import render, HttpResponse
from .models import Staff


# Create your views here.
def add_staff(request):
    staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': staff})


def save_staff(request):
    print("\nenter==================")
    if request.method == "POST":
        print("\n\nhello", request.POST.get('type'))
        print("\n\nhello", request.POST.get('doctor_name'))
        file = request.FILES['image']
        print("\n\nimage", file)
        staff = Staff(doctor_name=request.POST.get('doctor_name'),
                      type_treatment=request.POST.get('type'), doc_pic=file)
        staff.save()
        staff_rec = Staff.objects.all()
        HttpResponse ("Success")
    else:
        print("\n\nhello")


def view_staff(request):
    staff_rec = Staff.objects.all()
    for i in staff_rec:
        print("\n\n\nkljflks")
    return render(request, 'views_staff.html', {'staff_rec': staff_rec})