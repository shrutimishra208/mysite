from django.shortcuts import render, HttpResponse
from home.models import Contacts

def home(request):
    # return HttpResponse("This is my home.")
    context = {'name': 'shruti', 'course': 'django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my about page..")
    return render(request, 'about.html')

def contacts(request):
    if request.method=="Post":
        name = request.Post['name']
        email = request.Post['email']
        phone = request.Post['phone']
        # print(name,email,phone)
        ins = Contacts(name=name, email=email, phone=phone)
        ins.save()
        print("data has been written to the db")
    # return HttpResponse("This is my contacts page.")
    return render(request, 'contacts.html')

def project(request):
    # return HttpResponse("This is my project page.")
    return render(request, 'project.html')


# Create your views here.
