from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from store.models import Customer

# class ProfilePageView(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields =  ('user','name','email')
#         widgets = {
#                 'user': forms.TextInput(attrs={'class':'form-control'}),
#                 # 'profile_pic': forms.ImageField(),
#                 'name': forms.TextInput(attrs={'class':'form-control'}),
#                 'email': forms.TextInput(attrs={'class':'form-control'}),
#         }

# class EditProfileFormPage(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields =  ('user','name','email')
#         widgets = {
#                 'user': forms.TextInput(attrs={'class':'form-control'}),
#                 # 'profile_pic': forms.ImageField(),
#                 'name': forms.TextInput(attrs={'class':'form-control'}),
#                 'email': forms.TextInput(attrs={'class':'form-control'}),
#         }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email']
        labels={
            'first_name' : 'First Name',
            'last_name':'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

class EditProfileForm(UserChangeForm):
    date_joined = forms.CharField(max_length=100,disabled=True)
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','date_joined']
        labels={
            'first_name' : 'First Name',
            'last_name':'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined': forms.TextInput(attrs={'class':'form-control'}),
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(label='new password', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model =User
        fields = ['old_password','new_password1','new_password2']
       
