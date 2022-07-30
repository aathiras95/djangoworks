from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(label='Username')
    pwd=forms.CharField(label='Password')
class RegisterForm(forms.Form):
    fname = forms.CharField(label='First Name:')
    lname = forms.CharField(label='Last Name:')
    mail = forms.CharField(label='Email Id:')
    username = forms.CharField(label='UserName')
    pwd = forms.CharField(label='Password')
    rpwd = forms.CharField(label='Re-Enter your Password')
