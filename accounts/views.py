from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST["First_Name"]
        last_name = request.POST["Last_Name"]
        user_name = request.POST["User_Name"]
        mailid = request.POST["email"]
        pwd = request.POST["Password"]
        pwd1 = request.POST["Password1"]
        if pwd==pwd1 :
            if User.objects.filter(username=user_name).exists():
                #print("User Exist!")
                messages.error(request, "User Already Exist")
                return render(request, 'register.html')
            elif User.objects.filter(email=mailid).exists():
                #print("Mailid already Registe !")
                messages.info(request, "Mailid Already Register")
                return render(request, 'register.html')
            else:
                user=User.objects.create_user(username=user_name,password=pwd,email=mailid)
                user.save()
                print("User Created")
                return redirect('/')
        else:
            #print("Passwird Not Matching!")
            messages.info(request,"Password Not Matched")
            return render(request, 'register.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        user_name = request.POST["User_Name"]
        pwd = request.POST["Password"]
        user=auth.authenticate(username=user_name,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid")
            return redirect('login')
    else:
        return render(request, 'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')