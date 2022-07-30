from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import menu_items

# Create your views here.
class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        all_item=menu_items
        if 'category' in request.query_params:
            # category=request.query_params.get('category')
            # dish=[item for item in menu_items if item['category']==category]
            # return Response(data=dish)
            all_item=[ item for item in all_item if item['category']==request.query_params.get('category')]
        if 'limit' in request.query_params:
            limit=int(request.query_params.get('limit'))
            all_item=all_item[0:limit]
        if 'price_lt' in request.query_params:
            miniprice=int(request.query_params.get('price_lt'))
            all_item=[item for item in all_item if item['price']<=miniprice]
            return Response(data=all_item)
        return Response(data=menu_items)
    def post(self,request,*args,**kwargs):
        newdish=request.data
        menu_items.append(newdish)
        return Response(data=newdish)


class DishDetailView(APIView):
    def get(self,request,*args,**kwargs):
        dicode=kwargs.get('dcode')
        dish=[item for item in menu_items if item['code']==dicode].pop()
        return  Response(data=dish)
    def put(self,request,*args,**kwargs):
        code=kwargs.get(('dcode'))
        updata=[item for item in menu_items if item['code']==code].pop()
        data=request.data
        updata.update(data)
        return Response(data=data)
    def delete(self,request,*args,**kwargs):
        icode=kwargs.get('dcode')
        dish=[item for item in menu_items if item['code']==icode].pop()
        menu_items.remove(dish)
        return Response(data=dish)



