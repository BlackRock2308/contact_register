from django.shortcuts import render, get_object_or_404
from .models import Contact

def home(request):
    message = "Hello everyone"
    context = {'message' : message}
    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,'contact/contact_list.html',{'contacts': contacts})

def contact_details(request, id):
    contact = get_object_or_404(Contact, id = id)
    return render(request,'contact/contact_detail.html',{'contact': contact})


# Create your views here.
