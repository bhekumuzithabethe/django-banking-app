from django import forms
from .models import Transfare,Pay,Withdraw,Deposit

class PayForm(forms.ModelForm):
    class Meta:
        model =Pay
        fields = '__all__'

class TransfareForm(forms.ModelForm):
    class Meta:
        model =Transfare
        fields = '__all__'


class DepositForm(forms.ModelForm):
    class Meta:
        model =Deposit
        fields = '__all__'

class WithdrawForm(forms.ModelForm):
    class Meta:
        model =Withdraw
        fields =('card_number','amount')

