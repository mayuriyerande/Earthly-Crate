from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from app.models import Contact,User
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def index1(request):
    return render(request, 'index1.html')

def suggest(request):
    if request.method == "POST":
        
        messages.success(request,"your account has been created succesfully")
    return render(request, 'suggest.html')

def signup(request):
    if request.method == "POST":
        orgname = request.POST.get('orgname')
        usernames = request.POST.get('usernames')
        oname = request.POST.get('oname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(usernames,email,pass1)
        myuser.owner_name = oname
        myuser.save
        messages.success(request,"your account has been created succesfully")
    return render(request, 'loginuser.html')
          
   

def fashion(request):
    return render(request, 'fashion.html')

def products(request):
    return render(request, 'products.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def protective(request):
    return render(request, 'protective.html')

def corrugated(request):
    return render(request, 'corrugated.html')

def tissue(request):
    return render(request, 'tissue.html')

def contribute(request):
     return render(request, 'contribute.html')

def success(request):
    return render(request, 'success.html')

def carbon(request):
    return render(request, 'carbon.html')

def mushroom(request):
    return render(request, 'mushroom.html')

def ecobags(request):
    return render(request, 'ecobags.html')

def loginuser(request):
    if request.method == 'POST':
        usernames = request.POST.get('usernames')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username =usernames ,password=pass1)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request,"Please enter correct username or password, Try again")

    return render(request, 'loginuser.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact = Contact(name=name,email=email,subject=subject)
        contact.save()
        messages.success(request, 'Your message has been sent successfully. Thank you')
    return render(request, 'contact.html')