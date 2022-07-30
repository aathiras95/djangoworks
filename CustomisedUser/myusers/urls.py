from myusers import views
from django.urls import path,include
urlpatterns=[
    path("register",views.EmpCreateView.as_view(),name='signin'),
    path('',views.LoginView.as_view(),name='login')
]