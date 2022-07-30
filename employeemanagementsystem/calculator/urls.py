from django .urls import path
from calculator import views
urlpatterns=[
    path('home',views.HomeView.as_view(),name='calc-home'),
    path('add',views.AddView.as_view(),name='calc-add'),
    path('sub',views.SubView.as_view(),name='calc-sub'),
    path('mul',views.MultiplicationView.as_view(),name='calc-mul'),
    path('div',views.DivisionView.as_view(),name='calc-div'),
    path('fdiv',views.FdivisionView.as_view(),name='calc-fdiv'),
    path('rem', views.ModulusView.as_view(),name='calc-rem'),
    path('fact', views.FactView.as_view(),name='calc-fact'),
    path('wordcount',views.WordcountView.as_view(),name='calc-word'),
    path('prime',views.PrimeView.as_view(),name='calc-prime'),
]