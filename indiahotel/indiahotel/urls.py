"""indiahotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from hotel.views import DishesView,DishDetailsView,MenuItemsView,MenuItemDetailsView,UserRegisterView,DishViewsetView,DishModelViweSetsView
from products.views import ProductView,ProductDetailView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('dishes',DishViewsetView,basename='dishes')
router.register('mdishes',DishModelViweSetsView,basename='mdishes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/dishes/',views.DishesView.as_view()),
    path('hotels/dishes/<int:dcode>',views.DishDetailView.as_view()),
    path('api/v1/hotels/',DishesView.as_view()),
    path('api/v1/hotels/dishes/<int:id>',DishDetailsView.as_view()),
    path('products/product/',ProductView.as_view()),
    path('products/product/<int:id>',ProductDetailView.as_view()),
    path('api/v2/hotels/',MenuItemsView.as_view()),
    path('api/v2/hotels/dishes/<int:id>',MenuItemDetailsView.as_view()),
    path('api/v2/hotels/user/',UserRegisterView.as_view()),
    path('api/v2/token',obtain_auth_token)

]+router.urls
