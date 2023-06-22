from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user =authenticate(request, username=username, password=pass1)
        if user is  not None:
            authlogin(request,user)
            return redirect('/')
        else:
            return HttpResponse('user nmae or password is incorrect')
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('password did not match')
        my_user = User.objects.create_user(uname, email,pass1)
        my_user.save()
        return redirect('login')
        print(uname, email, pass1, pass2)
    
    return render (request, 'signup.html')


def Logout(request):
    logout(request)
    return redirect('login')