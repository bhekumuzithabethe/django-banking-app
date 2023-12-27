from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

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

class Consultant(models.Model):
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
