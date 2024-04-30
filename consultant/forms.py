from django import forms
from .models import Customer,Account,Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
        'expiry_date': forms.DateInput(attrs={'type': 'date'})

        }

    def __init__(self,*args, **kwargs):
        super(CardForm,self).__init__(*args, **kwargs)
        self.fields['account'].empty_label ='Select'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('__all__')

    def __init__(self,*args, **kwargs):
        super(AccountForm,self).__init__(*args, **kwargs)
        self.fields['account_holder'].empty_label ='Select'

class ClientForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'})

        }


