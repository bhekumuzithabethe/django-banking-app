from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

USER_TYPE_CHOICES = (
    ('','Select'),
    ('1','Admin'),
    ('2','Consultant'),
    ('3','Client'),

)
    
#User Model   
class User(AbstractUser):
    user_type = models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default='1')
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
