from django.urls import path
from .views import (
    client,
    transfare,
    pay,
    deposit,
    withdraw,
    client_transactions,
    update_client_user,
    )
urlpatterns = [
    path('home/',client,name='client'),
    path('update-profile/<int:id>/',update_client_user,name='update-profile'),
    
    path('transfare/',transfare,name='transfare'),
    path('pay/',pay,name='pay'),
    path('deposit/',deposit,name='deposit'),
    path('withdraw/',withdraw,name='withdraw'),
    path('account/<int:id>/',client_transactions,name='account'),

]
