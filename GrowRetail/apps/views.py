from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Image, VIPModel, MediumModel, LowModel

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform authentication logic here (e.g., check against database)
        # For simplicity, let's assume username is "admin" and password is "password"
        if username == 'admin' and password == '1234':
            request.session['username'] = username
            return redirect('index/')
        else:

            return render(request, 'login.html')

    return render(request, 'login.html')
def index(request):
    return render(request,'index.html')
def Vip(request):
    images = Image.objects.all()
    return render(request,'vip.html',{'images': images})
def Staff(request):
    images = Image.objects.all()
    return render(request,'staff.html',{'images': images})

def Automation(request):
    return render(request,'automation.html')

def Year(request):
    return render(request,'peak.html')
def satisfaction(request):
    images = Image.objects.all()
    return render(request,'satisfaction.html',{'images': images})
def alocater(request):
    return render(request,'alocater.html')