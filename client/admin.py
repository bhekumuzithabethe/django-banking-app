from django.contrib import admin
from .models import Transfare,Pay,Withdraw,Deposit,Transaction
# Register your models here.
admin.site.register(Transfare)
admin.site.register(Deposit)
admin.site.register(Transaction)
admin.site.register(Pay)
