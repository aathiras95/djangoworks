from django import forms
from django.forms import ModelForm
from blogapp .models import UserProfile,Blogs,Comments
from django .contrib.auth .models import User
from django .contrib .auth.forms import UserCreationForm

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
    username=forms.CharField()
    password=forms.CharField()

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        exclude=('user',)
        widgets={
            'date_of_birth':forms.DateInput(attrs={'type':'date'})

        }
class ResetPasswordForm(forms.Form):
    oldpassword=forms.CharField()
    newpassword=forms.CharField()
    confirmpassword=forms.CharField()

class ProfilePicUpdateForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=[

            'profile_pic'
        ]


class BlogsForm(ModelForm):
    class Meta:
        model=Blogs
        fields=[
            'title',
            'description',
            'image',
        ]

class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=[
            'comment',
        ]
        widgets={
            'comments':forms.TextInput()
        }