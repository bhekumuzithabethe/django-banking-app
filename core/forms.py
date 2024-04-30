from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User
  
class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model =User
        fields =('first_name','last_name','username','email','password1','password2')

class UpdateUserForm(UserChangeForm):
    class Meta:
        model =User
        fields =('first_name','last_name','username','email')

class AuthenticationForm(forms.Form):
    
    first_name = forms.CharField(
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        widget=forms.TextInput()
    )
    identity_number = forms.CharField(
        widget=forms.TextInput()
    )
        
