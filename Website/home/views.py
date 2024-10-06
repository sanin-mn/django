from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Docters
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request,'index.html')

 
def about(request):
    return render(request,'about.html')


def booking(request):
    form = BookingForm()
    form_details={
        'form' : form
    }
    return render(request,'booking.html', form_details)


def docters(request):
    doc_details={
        'docters' : Docters.objects.all()
    }
    return render(request,'docters.html', doc_details)


def contact(request):
    return render(request,'contact.html')
 

def department(request):
    dep_details={
        'dep' : Department.objects.all()
    }
    return render(request,'department.html', dep_details)
