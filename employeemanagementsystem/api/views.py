from django.shortcuts import render
from api .models import Employee
from rest_framework .response import Response
from api.serializer import EmployeemodelSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class Employeeview(APIView):
    def get(self,request,*args,**kwargs):
        employee=Employee.objects.all()
        serializer=EmployeemodelSerializer(employee,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=EmployeemodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class EmployeeDetailView(APIView):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get('eid')
        try:
            employe=Employee.objects.get(eid=eid)
            serializer=EmployeemodelSerializer(employe)
            return Response(data=serializer.data)
        except:
            return Response({'msg':'invalid'},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,*args,**kwargs):
        eid=kwargs.get('eid')
        instance=Employee.objects.get(eid=eid)
        serializer=EmployeemodelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self, request, *args, **kwargs):
        eid = kwargs.get('eid')
        try:
            employe = Employee.objects.get(eid=eid)
            employe.delete()
            return Response(data=request.data)
        except:
            return Response({'msg':'invalid'},status=status.HTTP_400_BAD_REQUEST)