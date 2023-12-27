from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
ACCOUNT_TYPE_CHOICES = [
    ('','Select'),
    ('TRUSAV','Savings'),
    ('CHQ','Cheque'),
    ('FIX','Fixed'),
]
CARD_TYPE_CHOICES = [
    ('','Select'),
    ('VISA','Visa'),
    ('MASTER','Master'),
    ('CREDIT','Credit'),
    ('DEBIT','Debit'),

]
GENDER_CHOICES = [
    ('','Select'),
    ('F','Female'),
    ('M','Male'),
]
TITLE_CHOICES = [
    ('','Select'),
    ('Ms','Miss'),
    ('Mrs','Missus'),
    ('Mr','Mister'),
    ('Dr','Doctor'),
    ('Prof','Professor'),
]

PROVINCE_CHOICES = [
    ('','Select'),
    ('MP','Mpumalanga'),
    ('GP','Gauteng'),
    ('NW','North West'),
    ('NC','Northen Cape'),
    ('EC','Eastern Cape'),
    ('WC','Western Cape'),
    ('FS','Free State'),
    ('LP','Limpopo'),
    ('KZN','Kwazulu Natal'),
]

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES)
    sex = models.CharField(max_length=15, choices=GENDER_CHOICES)
    cellphone = models.CharField(max_length=13,default='+27')
    date_of_birth = models.DateField()
    identity_number = models.CharField(max_length=13)
    address_line_1 = models.CharField(max_length=20)
    address_line_2 = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=4)
    province = models.CharField(max_length=10, choices=PROVINCE_CHOICES)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'Client: {self.first_name} {self.last_name}'
        
class Account(models.Model):    
    account_holder = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10,default=400159)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    balance =models.FloatField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.account_type} Account holder: {self.account_holder.first_name} {self.account_holder.last_name}'

class Card(models.Model):    

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16,default=44838500)
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)
    expiry_date = models.DateField()
    card_code_verification = models.CharField(max_length=3)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'Card holder: {self.account.account_holder.user.first_name} {self.account.account_holder.user.last_name}'
