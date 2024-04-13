from django.shortcuts import render,redirect
from .models import Branch, District
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
# Create your views here.def index(request):
def index(request):
    return render(request,'index.html')

def register(request):
    user=None
    error_message=None
    if request.POST:
        username =  request.POST['username']
        password =  request.POST['password']
        confirmpassword =  request.POST['confirmpassword']
        if password != confirmpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
            
            # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')

        else:
            user=User.objects.create_user(username=username,password=password)
            return redirect('login')

    return render(request,'register.html',{'user':user,'error_message':error_message})

def login(request):
    error_message=None
    if request.POST:
        username =  request.POST['username']
        password =  request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('services')
        else:
            error_message='invalid credentials'
    return render(request,'login.html',{'error_message':error_message})
    
def services(request):
    if request.method=='POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('accountType')
        materials_provided = request.POST.getlist('materials')
         # Display success message
        messages.success(request, 'Application accepted')
        
        # Redirect to index page after successful form submission
        return redirect('index')
    else:
        return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def logout(request):
    authlogout(request)
    return redirect('login')