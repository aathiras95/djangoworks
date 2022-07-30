from django.shortcuts import render,redirect
from django .views .generic import View,CreateView,FormView,TemplateView,UpdateView
from blogapp .forms import UserRegistrationForm,LoginForm,UserProfileForm,ResetPasswordForm,BlogsForm,CommentForm,ProfilePicUpdateForm
from django .contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from blogapp.models import UserProfile,Blogs,Comments
from django.contrib import messages


# Create your views here.
class SignUpView(CreateView):
    form_class=UserRegistrationForm
    template_name = 'signup.html'
    model=User
    success_url = reverse_lazy('login')

     # def get(self,request,*args,**kwargs):
     #     return render(request,'signup.html')
     # def post(self,request,*args,**kwargs):
     #     form=UserRegistrationForm(request.POST)
     #     if form.is_valid():
     #         form.save()
     #         return render(request,'login.html')
     #     else:
     #         return  render(request,'signup.html',{'form':form})

class LoginView(FormView):
    form_class = LoginForm
    template_name='login.html'
    model=User
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            print('success')
            login(request,user)
            return redirect('viewmyprofile')
        else:
            return render(request,'login.html')


class IndexView(CreateView):
    model=Blogs
    form_class = BlogsForm
    template_name ='home.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.instance.author=self.request.user
        self.object=form.save()
        messages.success(self.request,'post updated')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        blogs=Blogs.objects.all().order_by('-posted_date')
        context['blogs']=blogs
        comment_form=CommentForm()
        context['comment_form']=comment_form
        return context

class UserProfileAdd(CreateView):
    form_class=UserProfileForm
    template_name ='profilebio.html'
    model = UserProfile
    print('success')
    success_url=reverse_lazy('index')
    def form_valid(self,form):
        form.instance.user=self.request.user
        print(form.instance.user)
        self.object=form.save()
        messages.success(self.request, 'profile added')
        return super().form_valid(form)

class ViewMyProfileView(TemplateView):
    template_name = 'viewprofile.html'

class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'resetpassword.html'
    def post(self,request,*args,**kwargs):
        oldpassword=request.POST.get('oldpassword')
        password1=request.POST.get('newpassword')
        password2=request.POST.get('confirmpassword')
        user=authenticate(request,username=request.user.username,password=oldpassword)
        if user:
            user.set_password(password2)
            user.save()
            print(password2)
            messages.success(request, 'password changed successfully\nSigin In again to continue')
            return redirect('login')
        else:
            messages.error(request,'Invalid credential')
            return render(request,'resetpassword.html')

class UserUpdateView(UpdateView):
    model=UserProfile
    form_class = UserProfileForm
    template_name ='profileupdate.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg ='user_id'
    def form_valid(self, form):
        messages.success(self.request,'your profile updated Successfully')
        self.object = form.save()
        return super().form_valid(form)

class UserProfilePicUpdateView(UpdateView):
    model=UserProfile
    form_class = ProfilePicUpdateForm
    template_name = 'updateprofilepic.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'user_id'
    def form_valid(self, form):
        messages.success(self.request,'Profile pic update Successfully')
        self.object=form.save()
        return super().form_valid(form)

def SignOut(request,*args,**kwargs):
    logout(request)
    return redirect('login')


def addcomment(request,*args,**kwargs):
    if request.method=='POST':
        blog_id=kwargs.get('post_id')
        blog=Blogs.objects.get(id=blog_id)
        user=request.user
        comment=request.POST.get('comment')
        Comments.objects.create(blog=blog,user=user,comment=comment)
        messages.success(request,'comment added successfully')
        return redirect('index')

def addlikes(request,*args,**kwargs):
    blog_id=kwargs.get('post_id')
    blog=Blogs.objects.get(id=blog_id)

    blog.liked_by.add(request.user)
    blog.save()
    return redirect('index')

def removeblog(request,*args,**kwargs):
    blog_id=kwargs.get('post_id')
    blog=Blogs.objects.get(id=blog_id)
    blog.delete()
    messages.success(request,'Blog deleted')
    return redirect('index')





def follow_friend(request,*args,**kwargs):
    friend_id=kwargs.get('user_id')
    friend_profile=User.objects.get(id=friend_id)
    request.user.users.following.add(friend_profile)
    friend_profile.save()
    messages.success(request,'you are started to following'+friend_profile.username)
    return redirect('index')