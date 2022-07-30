from django .urls import path
from blogapp  import views
urlpatterns=[
    path('accounts/signup',views.SignUpView.as_view(),name='signup'),
    path('accounts/sigin',views.LoginView.as_view(),name='login'),
    path('accounts/signout',views.SignOut,name='signout'),
    path('index',views.IndexView.as_view(),name='index'),
    path('bio',views.UserProfileAdd.as_view(),name='profilebio'),
    path('users/profiles',views.ViewMyProfileView.as_view(),name='viewmyprofile'),
    path('changepassword',views.ResetPasswordView.as_view(),name='passwordchange'),
    path('user/profile/change/ <str:user_id>',views.UserUpdateView.as_view(),name='changeprofile'),
    path('user/profile/profilepic<str:user_id>',views.UserProfilePicUpdateView.as_view(),name='updatepropic'),
    path('post/comment/<int:post_id>',views.addcomment,name='add-comment'),
    path('post/like/add/<int:post_id>',views.addlikes,name='addlike'),
    path('post/remove/<int:post_id>',views.removeblog,name='delpost'),
    path('users//<int:user_id>',views.follow_friend,name='followfriend'),



]