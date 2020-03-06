from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Fort,ContactForm,Profile
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    forts = Fort.objects.all().order_by("-date_filled")
    # print(forts.count())o
    params = {
        'forts':forts,
        'media_url':settings.MEDIA_URL,
        'range':range(1,len(forts)+1),
    }
    return render(request,'app/index.html',params)

def fort(request,fort_name):
    fort = Fort.objects.get(name=fort_name)
    params = {
        'fort':fort,
        'media_url':settings.MEDIA_URL,

    }
    return render(request,"app/fort.html",params)

def contactUs(request):
    if request.method == "POST":
        name = request.POST["full_name"]
        email = request.POST["email_id"]
        contact = request.POST["contact_number"]
        message = request.POST["message"]
        ContactForm.objects.create(name=name,email=email,contact=contact,message=message)
    return render(request,"app/contact.html")

def signup(request):
    if request.method == "POST":
        try:
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            email = request.POST["email"]
            uname = request.POST["uname"]
            passwd = request.POST["passwd"]
            cpasswd = request.POST["cpasswd"]
            if passwd != cpasswd:
                messages.error(request,"Password and Confirmed Password should be Same!")
                return redirect('singup')
            else:
                user = User.objects.create_user(uname,email,passwd,first_name = fname,last_name=lname)
        except Exception:
            pass         
    return render(request,"app/signup.html")

def userLogin(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        passwd = request.POST["passwd"]
        user = authenticate(username=uname,password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successfull")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/')
    return render(request,"app/login.html")

def userLogout(request):
    logout(request)
    return redirect('/')

def about(request):
    profile = Profile.objects.all()
    params = {
        'profile':profile,
        'media_url':settings.MEDIA_URL,
    }
    return render(request,'app/about.html',params)