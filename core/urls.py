from django.urls import path
from .views import (
    login_view,
    logout_view,
    add_user,
    add_consultant,
    authenticate_bank_account_view,
    index
    )
urlpatterns = [
    #Authentication URL's
    path('',login_view,name='dologin'),
    #path('',index,name='index'),
    path('dologout/',logout_view,name='dologout'),

    path('create-user-account/',add_user,name='create-user-account'),
    path('create-consultant-account/',add_consultant,name='create-consultant-account'),

    path('authenticate-bank-account/',authenticate_bank_account_view,name='authenticate-bank-account'),

]
