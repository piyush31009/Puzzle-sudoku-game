from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(required=True, max_length=50)
    email=forms.EmailField(max_length=120, required=True,help_text='Required. Emter alid email address .')
    birth_date=forms.DateField(help_text="Required. Format: YYY-MM-DD", required=True)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','birth_date','password1','password2')