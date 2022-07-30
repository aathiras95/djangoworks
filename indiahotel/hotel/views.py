from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework.response import Response
from hotel.models import Dishes
from hotel.serializers import DishSerialiizer,DishesModelSerializer,UserRegistrationModelSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions,authentication

# Create your views here.
class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        all_dishes=Dishes.objects.all()
        serializer=DishSerialiizer(all_dishes,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=DishSerialiizer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            category=serializer.validated_data.get('category')
            price=serializer.validated_data.get('price')
            Dishes.objects.create(name=name,category=category,price=price)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class DishDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        dcode=kwargs.get('id')
        dish=Dishes.objects.get(id=dcode)
        serializer=DishSerialiizer(dish)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        dcode=kwargs.get('id')
        dish=Dishes.objects.get(id=dcode)
        dish.delete()
        return Response({"msd":"deleted the current"})
    def put(self,request,*args,**kwargs):
        dcode=kwargs.get('id')
        instance= Dishes.objects.get(id=dcode)
        serializer=DishSerialiizer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            category=serializer.validated_data.get('category')
            price = serializer.validated_data.get('price')
            instance.name=name
            instance.category=category
            instance.price=price
            instance.save()
            return Response(data=serializer.data)


class MenuItemsView(APIView):
    serializer_class=DishesModelSerializer
    def get(self,request,*args,**kwargs):
        all_dishes=Dishes.objects.all()
        serializer=self.serializer_class(all_dishes,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serilalizer=DishesModelSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(data=serilalizer.data)
        else:
            return Response(data=serilalizer.errors)

class MenuItemDetailsView(APIView):
    serializer_class=DishesModelSerializer
    def get(self,request,*args,**kwargs):
        dcode=kwargs.get('id')
        try:
            dish=Dishes.objects.get(id=dcode)
            serializer=DishesModelSerializer(dish)
            return Response(data=serializer.data)
        except:
            return Response({'msg':'invalid'},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,*args,**kwargs):
        dcode=kwargs.get('id')
        instance=Dishes.objects.get(id=dcode)
        serializer=self.serializer_class(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        dcode=kwargs.get('id')
        try:
            dish=Dishes.objects.get(id=dcode)
            dish.delete()
            return Response(data=request.data)
        except:
            return Response({'msg':'invalid'},status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    def get(self,request,*args,**kwargs):
        user=User.objects.all()
        serilaizer=UserRegistrationModelSerializer(user,many=True)
        return Response(data=serilaizer.data)
    def post(self,request,*args,**kwargs):
        serializer=UserRegistrationModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #
        #     first_name = serializer.validated_data.get('first_name')
        #     last_name = serializer.validated_data.get('last_name')
        #     email = serializer.validated_data.get('email')
        #     username = serializer.validated_data.get('username')
        #     password=serializer.validated_data.get('password')
        #
        #     User.objects.create(first_name =first_name,last_name=last_name,email=email,username=username,password=password)
        #
        #     return Response(data=serializer.data)
        #       User.objects.create_user(**serializer.validated_data)
            return Response(data=serializer.data)

class DishViewsetView(viewsets.ViewSet):
    # def list(self,request,*args,**kwargs):
    #     qs=Dishes.objects.all()
    #     serializer=DishesModelSerializer(qs,many=True)
    #     return Response(serializer.data)
    def list(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if 'category' in request.query_params:
            category=request.query_params.get('category')
            # qs=Dishes.objects.filter(category=category)
            # serializer=DishesModelSerializer(qs,many=True)
            # return Response(serializer.data)
            qs=qs.filter(category=category)
        if 'price-lt' in request.query_params:
            price=request.query_params.get('price_lt')
            qs=qs.filter(price__lte=price)

        serializer=DishesModelSerializer(qs,many=True)
        print(serializer)
        return Response(serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=DishesModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Dishes.objects.get(id=id)
        serializer=DishesModelSerializer(qs)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        instance=Dishes.objects.get(id=id)
        serializer = DishesModelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        dishes=Dishes.objects.get(id=id)
        dishes.delete()
        return Response({'msg':'deleted'})

class DishModelViweSetsView(viewsets.ModelViewSet):
    serializer_class=DishesModelSerializer
    queryset = Dishes.objects.all()
    medel=Dishes
    # authentication_classes = [authentication.BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

