from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if email=='':
            messages.add_message(request,messages.ERROR,"Email field cannot be empty")
            return redirect("/auth/signup")

        if password!=confirmpassword:
            messages.add_message(request,messages.ERROR,"Passwords mismatch")
            return redirect("/auth/signup")
            
        else:
            user = User.objects.create_user(email,password=password)
            user.save()
            return redirect("/")
    return render(request,"signup.html")



def signin(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            print('validdddddddddd ')
            login(request,user)
            return redirect("/")
        else:
            print('invalid credentials')

    return render(request,"signin.html")


def signout(request):
    logout(request)
    return redirect("/")