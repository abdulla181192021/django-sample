from django import forms
from django.contrib.auth.models import User
from auth_app.models import Userinfo

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class userinfo(forms.ModelForm):
    class Meta():
        model=Userinfo
        fields=('facebook_id','profile_pic')
