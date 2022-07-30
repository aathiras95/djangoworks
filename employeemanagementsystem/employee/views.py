from django.shortcuts import render,redirect
from django .http import HttpResponse
from django .views.generic import View
from  employee .forms import LoginForm
from employee.forms import RegisterForm
from employee.models import Employee
from employee .forms import EmployeeForm
from django.contrib import messages
from employee.forms import UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.
# def index(request):
#     # return HttpResponse("<h1>welcome</h1>")
#     return render(request,'home.html')
#
#
# def register_user(request):
#     return HttpResponse("<h1>Create account here</h1>")
#
# def login(request):
#     return  render(request,"login.html")

# class IndexView(View):
#     def get(self,request):
#         return render(request,'home.html')
#
# class LoginView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,'login.html',{'form':form})
#     def post(self,request):
#         print(request.POST.get('username'))
#         print(request.POST.get('pwd'))
#         return render(request,'login.html')
#
# class RegisterView(View):
#     def get(self,request):
#         form=RegisterForm()
#         return render(request,'register.html',{'form':form})
#     def post(self,request):
#         print(request.POST.get('fname'))
#         print(request.POST.get('lname'))
#         print(request.POST.get('mail'))
#         print(request.POST.get('username'))
#         print(request.POST.get('pwd'))
#         print(request.POST.get('rpwd'))
#         return render(request,'register.html')

# class EmployeeCreateView(View):
#     form_class=EmpolyeeForm
#     template_name="emp_add.html"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})
#
#     def post(self,request):
#         form=self.form_class(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             print("clened data")
#             print(form.cleaned_data)
#             print(form.cleaned_data.get('eid'))
#             print(form.cleaned_data.get('employee_name'))
#             print(form.cleaned_data.get('designation'))
#             print(form.cleaned_data.get('email'))
#             print(form.cleaned_data.get('salary'))
#             print(form.cleaned_data.get('experience'))
#             # return render(request,self.template_name,{'form':form})
#             messages.success(request,'Profile Added')
#             return redirect('emp_add')
#
#         else:
#             messages.error(request,' Cant add profile' )
#             return render(request,self.template_name,{'form':form})
def signin_required(fuctn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fuctn(request,*args,**kwargs)
        else:
            messages.error(request,'Sigin First')
            return  redirect('login')
    return wrapper


@method_decorator(signin_required,name='dispatch')
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeForm()
        return render(request,'emp_add.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employee.objects.create(
            #     eid=form.cleaned_data.get('eid'),
            #     employee_name=form.cleaned_data.get('employee_name'),
            #     designation=form.cleaned_data.get('designation'),
            #     salary=form.cleaned_data.get('salary'),
            #     email=form.cleaned_data.get('email'),
            #     experience=form.cleaned_data.get('experience')
            # )
            messages.success(request,'Profile added sucessfully')
            return redirect('emp_add')
        else:
            messages.error(request,'Profile adding Failed')
            return render(request, 'emp_add.html', {'form': form})

@method_decorator(signin_required,name='dispatch')
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            qs=Employee.objects.all()
            return render(request,'emp_list.html',{'employees':qs})
        else:
            messages.error(request,'login failed')
            return redirect('login')
@method_decorator(signin_required,name='dispatch')
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.get(eid=kwargs.get('emp_id'))
        return render(request,'emp_details.html',{'employe':qs})

@method_decorator(signin_required,name='dispatch')
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        e_id=kwargs.get('emp_id')
        employe=Employee.objects.get(eid=e_id)
        form=EmployeeForm(instance=employe)
        return render(request,'emp_edit.html',{'employe':form,'qs':employe})
    def post(self,request,*ars,**kwargs):
        e_id = kwargs.get('emp_id')
        employe = Employee.objects.get(eid=e_id)
        form = EmployeeForm(request.POST,instance=employe,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Edited sucessfully')
            return redirect('emp_list')
        else:
            messages.error(request, 'Profile Editing failed Failed')
            return render(request, 'emp_edit.html', {'employe': form})

@signin_required
def remove(request,*args,**kwargs):
    e_id=kwargs.get('emp_id')
    employe=Employee.objects.get(eid=e_id)
    employe.delete()
    messages.success(request,'profile Deleted')
    return redirect('emp_list')

def index(request):
    return render(request,'base.html')


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,'registration.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'registerd Successfully')
            return redirect('login')

        else:
            messages.error(request,'registerd UnSuccessfully')
            return render(request,'registration.html',{'form':form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print('success')
                return redirect('emp_list')
            else:
                messages.error(request,'Invalid Credential')
                return render(request, 'login.html', {'form': form})


@signin_required
def Signout(request,*args,**kwargs):
    logout(request)
    return redirect('login')





