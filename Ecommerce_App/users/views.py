from django.shortcuts import render
from django .views.generic import View
from users .forms import LoginForm
from users .forms import RegisterForm

from django .http import HttpResponse

# Create your views here.
# Fuctional view

# def login(request):
#     return HttpResponse("<h2>Login Here</h2>")
#
# def about_home(request):
#     return HttpResponse("<h3>Welcome To ecom App </h3>")
#
# def signup(request):
#     return HttpResponse("<h4>Register Here !!!</h4>")


# class based view
class UserHomeView(View):
    def get(self,request):

        return render(request,'home.html')

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return  render(request,'login_user.html',{'form':form})
    def post(self,request):
        print(request.POST.get('user_name'))
        print(request.POST.get('pwd'))
        return render(request,'login_user.html')


class RegisterView(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'register_user.html',{'form':form})
    def post(self,request):
        print(request.POST.get('f_name'))
        print(request.POST.get('l_name'))
        print(request.POST.get('e_mail'))
        print(request.POST.get('user_name'))
        print(request.POST.get('pwd'))
        print(request.POST.get('re_pwd'))
        return render(request,'register_user.html')
