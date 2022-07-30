from django.shortcuts import render
from rest_framework .response import Response
from rest_framework.views import APIView
from products .sreializers import ProdcutSerializer
from products.models import Products

# Create your views here.
class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        all_product=Products.objects.all()
        serializer=ProdcutSerializer(all_product,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        # product=request.data
        serializer=ProdcutSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            spec=serializer.validated_data.get('spec')
            price=serializer.validated_data.get('price')
            Products.objects.create(name=name,spec=spec,price=price)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        serializer=ProdcutSerializer(product)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        product.delete()
        return Response({'msg':'Deleted'})