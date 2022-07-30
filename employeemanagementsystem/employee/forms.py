from django import forms
from employee.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(forms.Form):
    fname=forms.CharField(label='First Name:')
    lname=forms.CharField(label='Last Name:')
    mail=forms.CharField(label='Email Id:')
    username=forms.CharField(label='UserName')
    pwd = forms.CharField(label='Password')
    rpwd = forms.CharField(label='Re-Enter your Password')


# class EmpolyeeForm(forms.Form):
#     eid = forms.CharField(label='Employee Id:',widget=forms.TextInput(attrs={'class':"form-control"}))
#     employee_name = forms.CharField(label='Employee Name:',widget=forms.TextInput(attrs={'class':"form-control"}))
#     designation = forms.CharField(label='Designation',widget=forms.TextInput(attrs={'class':"form-control"}))
#     salary = forms.IntegerField(label='Salary',widget=forms.NumberInput(attrs={'class':"form-control"}))
#     email = forms.EmailField(label='Email Id:',widget=forms.EmailInput(attrs={'class':"form-control"}))
#     experience= forms.IntegerField(label='Experience',widget=forms.NumberInput(attrs={'class':"form-control"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         experience=cleaned_data.get('experience')
#         if experience<0:
#             msg='invalid exp'
#             self.add_error('experience',msg)


# class EmployeeForm(forms.Form):
#     eid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets={
            'eid':forms.TextInput(attrs={'class':'form-control'}),
            'employee_name':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'})


        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',

        ]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))