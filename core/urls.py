from django.urls import path
from .views import (
    login_view,
    logout_view,
    add_user,
    add_consultant,
    update_user,
    authenticate_bank_account_view,
    )
urlpatterns = [
    #Authentication URL's
    path('',login_view,name='dologin'),
    path('logout/',logout_view,name='dologout'),

    path('create-user-account/',add_user,name='create-user-account'),
    path('create-consultant-account/',add_consultant,name='create-consultant-account'),

    path('update-user/<int:id>/',update_user,name='update-user'),
    path('authenticate-bank-account/',authenticate_bank_account_view,name='authenticate-bank-account'),

]
