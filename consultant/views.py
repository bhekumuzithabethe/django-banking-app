from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer,Account,Card
from core.models import User
from core.forms import UpdateUserForm
from bank_mananger.models import Consultant
from client.models import Transaction


#Imports from forms.py
from .forms import (
    AccountForm,
    ClientForm,
    CardForm,
    )

# Create your views here.

#Admin views
@login_required()
def consultant(request):
    users = User.objects.all()
    no_of_users = users.__len__()

    clients = Customer.objects.all()
    no_of_clients = clients.__len__()

    consultants = Consultant.objects.all()
    no_of_consultants = consultants.__len__()

    accounts = Account.objects.all()
    no_of_accounts = accounts.__len__()

    cards = Card.objects.all()
    no_of_cards = cards.__len__()
    clients = Customer.objects.all()

    return render(request,"consultant/consultant.html",{
        'no_of_users':no_of_users,
        'no_of_clients':no_of_clients,
        'no_of_consultants':no_of_consultants,
        'no_of_accounts':no_of_accounts,
        'no_of_cards':no_of_cards,
        'clients':clients,
    })
@login_required()
def add_client(request):
    
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, 'You have successfully created a client.')
            return redirect('manage-clients')
    
        else:
            messages.error(request, 'Failed to create client.')
            return redirect('add-client')
    else:
        form = ClientForm()
        return render(request,"consultant/forms/add_client.html",{
            'form':form,
        })
@login_required()  
def update_client(request,id):
    if request.method=='POST':
        client = Customer.objects.get(pk=id)
        form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            client = form.save()
            messages.success(request, "You have successfully updated the client's details.")
            return redirect('manage-clients')
        else:
            messages.error(request, "Failed to update client details.")
            return redirect('update-client',id)
    else:
        client = Customer.objects.get(pk=id)
        form = ClientForm(instance=client)
        return render(request,"consultant/forms/update_client.html",{
            'form':form,
            'client':client,
        })
@login_required()
def manage_clients(request):
    clients = Customer.objects.all()
    return render(request,"consultant/manage/manage_clients.html",{
        'clients':clients,
    })
@login_required()
def delete_client(request,id):
    client = Customer.objects.get(pk=id)
    client.delete()
    messages.success(request, 'Client successfully deleted.')
    return redirect('manage-clients')











@login_required()
def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            messages.success(request, "You have successfully created a client's account.")
            return redirect('manage-accounts')
        else:
            messages.error(request, "Failed to create client's account.")
            return redirect('add-account')
    else:
        form = AccountForm()
        return render(request,"consultant/forms/add_account.html",{
            'form':form,
        })
@login_required() 
def update_account(request,id):
    if request.method=='POST':
        account = Account.objects.get(pk=id)
        form = AccountForm(request.POST,instance=account)
        if form.is_valid():
            account = form.save()
            messages.success(request, "You have successfully updated the client's account details.")
            return redirect('manage-accounts')
        else:
            messages.error(request, "Failed to update client's account details.")
            return redirect('update-account',id)
    else:
        account = Account.objects.get(pk=id)
        form = AccountForm(instance=account)
        return render(request,"consultant/forms/update_account.html",{
            'form':form,
            'account':account,
        })
@login_required()
def manage_accounts(request):
    accounts = Account.objects.all()
    return render(request,"consultant/manage/manage_accounts.html",{
        'accounts':accounts,
    })
@login_required()
def delete_account(request,id):
    account = Account.objects.get(pk=id)
    account.delete()
    messages.success(request, "You have successfully deleted the client's account.")
    return redirect('manage-accounts')
@login_required()
def add_card(request):
    if request.method=='POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            messages.success(request, "You have successfully created a client's card.")
            return redirect('manage-cards')
        else:
            messages.error(request, "Failed to create client's card.")
            return redirect('add-card')
    else:
        form = CardForm()
        return render(request,"consultant/forms/add_card.html",{
            'form':form,
        })
@login_required()   
def update_card(request,id):
    if request.method=='POST':
        card = Card.objects.get(pk=id)
        form = CardForm(request.POST,instance=card)
        if form.is_valid():
            card = form.save()
            messages.success(request, "You have successfully updated the client's card details.")
            return redirect('manage-cards')
        else:
            messages.error(request, "Failed to update client's card details.")
            return redirect('update-card',id)
    else:
        card = Card.objects.get(pk=id)
        form = CardForm(instance=card)
        return render(request,"consultant/forms/update_card.html",{
            'form':form,
            'card':card,
        })
@login_required()
def manage_cards(request):
    cards = Card.objects.all()
    return render(request,"consultant/manage/manage_cards.html",{
        'cards':cards,
    })
@login_required()
def delete_card(request,id):
    card = Card.objects.get(pk=id)
    card.delete()
    messages.success(request, "You have successfully deleted client's card.")
    return redirect('manage-cards')

@login_required()
def consultant_client_transactions_view(request,id):
    account = Account.objects.get(pk=id)
    transactions = Transaction.objects.filter(account_number=account.account_number).all()
      
    return render(request,"consultant/transactions.html",{
        'transactions':transactions,

    })



@login_required()
def update_profile(request,id):
    if request.method=='POST':
        user = User.objects.get(pk=id)
        form = UpdateUserForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have successfully updated your user account's details.")
            return redirect('consultant')
        else:
            messages.error(request, "Failed to update user details.")
            return redirect('update-consultant-profile',id)
    else:
        user = User.objects.get(pk=id)
        form = UpdateUserForm(instance=user)
        return render(request,"consultant/forms/update_user.html",{
            'form':form,
            'user':user,

        })




    

