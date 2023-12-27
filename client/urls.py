from django.urls import path
from .views import (
    client,
    transfare,
    pay,
    deposit,
    withdraw,
    client_transactions,
    )
urlpatterns = [
    path('home/',client,name='client'),
    
    path('transfare/',transfare,name='transfare'),
    path('pay/',pay,name='pay'),
    path('deposit/',deposit,name='deposit'),
    path('withdraw/',withdraw,name='withdraw'),
    path('account/<int:id>/',client_transactions,name='account'),

]
