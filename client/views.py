from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transfare,Pay,Withdraw,Deposit,Transaction
from core.models import User
from core.forms import UpdateUserForm
from consultant.models import Account,Customer
#Imports from forms.py
from .forms import (
    WithdrawForm,
    TransfareForm,
    PayForm,
    DepositForm,
    )

# Create your views here.
@login_required()
def client(request):
    user = request.user
    client = Customer.objects.get(first_name=user.first_name,last_name=user.last_name)
    accounts = Account.objects.filter(account_holder=client).all()        
   
    return render(request,"client/client.html",{
        'accounts':accounts,
        'user':user,
    })
@login_required()
def pay(request):
    user = request.user
    client = Customer.objects.get(first_name=user.first_name,last_name=user.last_name)
    accounts = Account.objects.filter(account_holder=client).all()
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            from_account = request.POST['from_account'] 
            #getting the senders account
            account = Account.objects.get(account_number=from_account)

            to_account = form.cleaned_data['to_account']
            reference = form.cleaned_data['reference']
            amount = form.cleaned_data['amount']

            if account.balance>=float(amount):
                account.balance -= float(amount)
                account.save()

                pay_account = Account.objects.get(account_number=to_account)
                pay_account.balance += float(amount)
                pay_account.save()

                transaction = Transaction.objects.create(transaction_type='Pay',account_number=from_account,amount=amount)
                transaction = Transaction.objects.create(transaction_type='Deposit',account_number=to_account,amount=amount)
                amount = str(amount)
                messages.success(request,"R"+amount+" payed successfully to ("+to_account+") account.")
                return redirect('client')
            else:
                messages.error(request, "Insufficient funds.")
                return redirect('pay')
        else:
            messages.error(request, "Failed to pay R"+amount+" "+to_account+")")
            return redirect('pay')
    else:
        form = PayForm()
        return render(request, "client/pay.html",{
            'form':form,
            'accounts':accounts,
        })

@login_required()
def transfare(request):
    user = request.user
    client = Customer.objects.get(first_name=user.first_name,last_name=user.last_name)
    accounts = Account.objects.filter(account_holder=client).all()
    if request.method == 'POST':
        from_account = request.POST['from_account'] 
        to_account = request.POST['to_account'] 
        reference = request.POST['reference'] 
        amount = request.POST['amount']
        sender_account = Account.objects.get(account_holder=client,account_number=from_account)    

        if sender_account.balance>=float(amount):
           reciever_account = Account.objects.get(account_number=to_account)

           reciever_account.balance += float(amount)
           reciever_account.save()
               
           
           sender_account.balance -= float(amount)
           sender_account.save()

           sender_account_number = str(sender_account.account_number)
               
           #Creating a transaction of type Transfer for the sender
           transaction = Transaction.objects.create(transaction_type='Transfer',account_number=sender_account_number,amount=amount)
           #Creating a transaction of type Deposit for the reciever
           transaction = Transaction.objects.create(transaction_type='Deposit',account_number=reciever_account.account_number,amount=amount)
           transaction.save()
            
           messages.success(request,"R"+amount+" Transfered successfully to ("+to_account+") account")
           return redirect('client')
        elif sender_account.account_type == 'FIX':
               messages.error(request, "Transaction not suitable for this account.")
        else:
            messages.error(request, "Insufficient funds.")
            return redirect('transfare')
               
        
    else:
        form = TransfareForm()
        return render(request,"client/transfare.html",{
            'form':form,
            'accounts':accounts,
        })   
@login_required()    
def deposit(request):
    if request.method =='POST':
        form = DepositForm()
        
        account_number = request.POST['account_number']
        reference = request.POST['reference']
        amount = request.POST['amount']

        account_deposit = Account.objects.get(account_number=account_number)

        account_deposit.balance += float(amount)
        account_deposit.save()
        #Creating a transaction of type Deposit
        transaction = Transaction.objects.create(transaction_type='Deposit',account_number=account_number,amount=amount)
        transaction.save()
            
        messages.success(request,"R"+amount+" Deposited to "+account_number+" successfully.")
        return redirect('client')            
    else:
        form = DepositForm()
    return render(request,"client/deposit.html",{
        'form':form,
    })
@login_required()
def withdraw(request):
    user = request.user
    client = Customer.objects.get(first_name=user.first_name,last_name=user.last_name)
    accounts = Account.objects.filter(account_holder=client).all()
    if request.method == 'POST':
        account_number = request.POST['account']
        form = WithdrawForm(request.POST)
        card_number = request.POST['card_number']
        amount = request.POST['amount']

        if form.is_valid():
           card_number = request.POST['card_number'] 
           amount = request.POST['amount']
           account = Account.objects.get(account_number=account_number)

           if account.account_type == 'CHQ' or account.account_type == 'TRUSAV':
                if account.balance>=float(amount):
                    
                    account.balance = account.balance - float(amount)
                    account.save()


                    account_number = str(account.account_number)

                    #Creating a transaction of type Withdrawal
                    transaction = Transaction.objects.create(transaction_type='Withdrawal',account_number=account_number,card_number=card_number,amount=amount)
                    transaction.save()
                    
                    messages.success(request,"R"+amount+" Withdrawn successfully.")
                    return redirect('client')
                else:
                    messages.error(request, "Insufficient funds.")
                    return redirect('withdraw')
           else :
               messages.error(request, "Transaction not suitable for this account.")
           
        else:
            messages.error(request, "Withdrawal failed.")
            return redirect('withdraw')

    else:
        form = WithdrawForm()
        return render(request,"client/withdraw.html",{
            'form':form,
            'accounts':accounts,
        })   
@login_required()
def client_transactions(request,id):
    account = Account.objects.get(pk=id)
    transactions = Transaction.objects.filter(account_number=account.account_number).all()
      
    return render(request,"client/transactions.html",{
        'transactions':transactions,

    })


@login_required()
def update_client_user(request,id):
    if request.method=='POST':
        user = User.objects.get(pk=id)
        form = UpdateUserForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have successfully updated your user account's details.")
            return redirect('client')
        else:
            messages.error(request, "Failed to update user details.")
            return redirect('update-profile',id)
    else:
        user = User.objects.get(pk=id)
        form = UpdateUserForm(instance=user)
        return render(request,"client/update_user.html",{
            'form':form,
            'user':user,

        })


