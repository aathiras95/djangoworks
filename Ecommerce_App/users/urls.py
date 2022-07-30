from django .urls import path
from users import views
# url for functional views

# urlpatterns=[
#     path('login',views.login),
#     path('home',views.about_home),
#     path('Register',views.signup)
# ]


# url for class based view

urlpatterns=[
    path('home',views.UserHomeView.as_view(),name='user_home'),
    path("login",views.LoginView.as_view(),name='user_login'),
    path('register',views.RegisterView.as_view(),name='user_register')
]