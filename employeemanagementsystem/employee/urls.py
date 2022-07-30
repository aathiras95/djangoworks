from django .urls import path
from employee import views
urlpatterns=[
    # path("index",views.index),
    # path("signup",views.register_user),
    # path("login",views.login)
#     path("index",views.IndexView.as_view(),name='emp-home'),
#     path("login",views.LoginView.as_view(),name='emp-login'),
#     path('register',views.RegisterView.as_view(),name='emp-register'),
#     path('profile/add',views.EmployeeCreateView.as_view(),name='emp_add')
      path('add',views.EmployeeCreateView.as_view(),name='emp_add'),
      path('all',views.EmployeeListView.as_view(),name='emp_list'),
      path('details/<str:emp_id>',views.EmployeeDetailView.as_view(),name='emp_details'),
      path('change/<str:emp_id>',views.EmployeeEditView.as_view(),name='emp_edit'),
      path('remove/<str:emp_id>',views.remove,name='emp_delete'),
      path('',views.index,name='index'),
      path('accounts/signup',views.SignUpView.as_view(),name='sign-up'),
      path('accounts/login',views.LoginView.as_view(),name='login'),
      path('accounts/signout',views.Signout,name='sign-out')


 ]