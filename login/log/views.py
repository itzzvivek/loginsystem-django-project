from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def home(request):
    return render(request, "home.html")


def handleSignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username) < 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        #create the user

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, "Your are registered successfully")
        return redirect('home')

    else:
        return HttpResponse("404 - NOt found")

        return HttpResponse("home")


def handleLogin(request):
    if request.method=='POST':
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']

      user = authenticate(username=loginusername, password=loginpassword)
      if user is not None:
          login(request, user)
          messages.success(request, "Successfully Logged In")
          return redirect("home")
      else:
          messages.error(request, "Invalid credentials! Please try again")
          return redirect("home")

    return HttpResponse("404- Not found")

    return HttpResponse("home")


def handleLogout(request):
    logout(request)
    messages.success(request, "Sucessfully logged out")
    return redirect('home')





