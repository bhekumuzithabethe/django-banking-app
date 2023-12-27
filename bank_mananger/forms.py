from django import forms
from .models import Consultant



class ConsultantForm(forms.ModelForm):

    class Meta:
        model = Consultant
        fields = '__all__'
        widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'})

        }
