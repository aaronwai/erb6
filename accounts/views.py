from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists !")
                return redirect("accounts:register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists !")
                    return redirect("accounts:register")
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request, "Account created successfully !")
                    return redirect("accounts:login")
        else:
            messages.error(request, "Passwords do not match !")
            return redirect("accounts:register")    
    else:    
        return render(request,'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are now logged in !")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid credentials !")
            return redirect("accounts:login")
    else :
        return render(request,'accounts/login.html')

def logout(request):
    return redirect("pages:index")

def dashboard(request):
    return render(request,'accounts/dashboard.html')