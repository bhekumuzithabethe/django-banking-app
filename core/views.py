from django.shortcuts import render, redirect

from .models import User
from bank_mananger.models import Consultant
from consultant.models import Customer
#Authentication imports
from django.contrib.auth import (
    login,
    logout,
    authenticate
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#Imports from forms.py
from .forms import (
    CreateUserForm,
    LoginForm,
    AuthenticationForm,
    UpdateUserForm,
    )

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if User.objects.filter(username=username).exists() and User.objects.filter(password=password).exists:
                if user is not None and user.user_type == '1':
                    login(request,user)
                    return redirect('adminpage')
                elif user is not None and user.user_type == '2':
                    login(request,user)
                    return redirect('consultant')
                elif user is not None and user.user_type == '3':
                    login(request,user)
                    return redirect('client')
                else:
                    messages.error(request, "Invalid username or password.")
                    return redirect('dologin')
            else:
               messages.error(request, "Username does not exist.")
               return redirect('dologin')            
        else:
            messages.error(request, "Failed to login.")
            return redirect('dologin')
    else:
        form = LoginForm()
        return render(request,"login/login.html",{
            'form':form,
        }) 
@login_required()
def logout_view(request):
    logout(request)
    return redirect('dologin')


def authenticate_bank_account_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        identity_number = request.POST['identity_number']

        if Customer.objects.filter(last_name=last_name).exists() and Customer.objects.filter(first_name=first_name).exists() and Customer.objects.filter(email=email).exists() and Customer.objects.filter(identity_number=identity_number).exists():
            return redirect('create-user-account')
        elif Consultant.objects.filter(last_name=last_name).exists() and Consultant.objects.filter(first_name=first_name).exists() and Consultant.objects.filter(email=email).exists() and Consultant.objects.filter(identity_number=identity_number).exists():
            return redirect('create-consultant-account')
        else:
            messages.error(request, "It seems as if you don't have a bank account with us, please try visiting our branch near to you to open a banking account with us. Thank you.")
            return redirect('authenticate-bank-account')

    else:
        form = AuthenticationForm()
        return render(request,"login/authenticate_bank_account.html",{
            'form':form,
        })

def add_user(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('create-user-account')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('create-user-account')
        else:
            if password1 == password2:
                #if form.is_valid():
                new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,user_type='3')
                login(request,new_user)
                return redirect('client')
                #else:
                messages.error(request, 'Failed to create user account.')
                #return redirect('manage-users')
            else:
                messages.error(request, "Passwords don't match.")
                return redirect('create-user-account')

    else:
        form = CreateUserForm()
        return render(request,"login/create_user_account.html",{
            'form':form,
        })


def add_consultant(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('create-consultant-account')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('create-consultant-account')
        else:
            if password1 == password2:
                if form.is_valid():
                    new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,user_type='2')
                    new_user.save()
                    login(request,new_user)
                    return redirect('consultant')
                else:
                    messages.error(request, 'Failed to create user account.')
                    return redirect('create-consultant-account')
            else:
                messages.error(request, "Passwords don't match.")
                return redirect('create-consultant-account')

    else:
        form = CreateUserForm()
        return render(request,"login/create_consultant_account.html",{
            'form':form,
        })

def index(request):
    return render(request,"client/index.html")