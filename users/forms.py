from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Tên Đăng Nhập",  
                "value"       : "",              
                "class"       : "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Mật Khẩu",
                "value"       : "",           
                "class"       : "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Tên Đăng Nhập",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Mật Khẩu",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Nhập Lại Mật Khẩu",                
                "class": "form-control"
            }
        ))

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),         
        empty_label = 'Chọn Bộ Phận',
        widget=forms.Select(
            attrs={
                "class": "selectpicker",
                "data-style": "btn btn-primary btn-round"
            }
        ),             
        required=True
        )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'group')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'aboutme']

