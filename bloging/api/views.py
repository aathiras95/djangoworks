from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import users,blogs

# Create your views here.
class UserView(APIView):
    def get(self,*args,**kwargs):
        return Response(data=users)
    def post(self,request,*args,**kwargs):
        user=request.data
        users.append(user)
        return Response(data=user)

class DetailedUserView(APIView):
    def get(self,request,*args,**kwargs):
        uid=kwargs.get('ucode')
        user=[user for user in users if user['id']==uid]
        return Response(data=user)

class BlogView(APIView):
    def get(self,*args,**kwargs):
        return Response(data=blogs)
    def post(self,request,*args,**kwargs):
        blog=request.data
        blogs.append(blog)
        return Response(data=blog)


class DetailedBlogView(APIView):
    def get(self,request,*args,**kwargs):
        blcode=kwargs.get('bcode')
        blog=[blog for blog in blogs if blog['postId']==blcode].pop()
        return Response(data=blog)

