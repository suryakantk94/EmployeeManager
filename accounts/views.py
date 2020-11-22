from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def registerUser(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1= request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        

        print(username,first_name)
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password1, email=email)

        user.save();
        print('user created')
        return redirect("/")
    else:
        print("error")    
        return render(request, 'register.html')    

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            print("authenticated")
            return redirect("/")
        else:
            print("NOT authenticated")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")