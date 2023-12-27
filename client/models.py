from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Transfere Model      
class Transfare(models.Model):
    from_account = models.CharField(max_length=10)
    to_account = models.CharField(max_length=10)
    reference = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self) -> str:
        return f'{self.account_number} Transfared R{self.amount} to: {self.account_number} on {self.transfare_date}.'

class Pay(models.Model):
    to_account = models.CharField(max_length=10)
    reference = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self) -> str:
        return f'{self.account_number} Transfared R{self.amount} to: {self.account_number} on {self.transfare_date}.'

   
#Transfere Model      
class Deposit(models.Model):
    account_number = models.CharField(max_length=10)
    reference = models.CharField(max_length=15)
    deposit_date = models.DateField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self) -> str:
        return f'R{self.amount} Deposit to: {self.account_number} on {self.deposit_date}.'

#Withdraw Model   
class Withdraw(models.Model):
    account = models.CharField(max_length=17)
    card_number = models.CharField(max_length=16)
    amount = models.FloatField()

    def __str__(self) -> str:
        return f'{self.card_number} Withdrew R{self.amount} on {self.withdrawal_date}.'
    
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10,null=True,blank=True)
    card_number = models.CharField(max_length=16,null=True,blank=True)
    amount = models.FloatField()
    transaction_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'R{self.amount} {self.transaction_type}'