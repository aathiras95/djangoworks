import re

from django.shortcuts import render
from django .views.generic import View
from calculator .forms import OperationForm

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'calc_home.html')

class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        # sum=int(n1)+int(n2)
        # print('sum:',sum)
        # form1=OperationForm()
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get('num1')
            n2=form.cleaned_data.get('num2')
            sum=n1+n2
            # print(form.cleaned_data)
            return render(request,'add.html',{'result':sum,'form':form})
        else:
            return render(request,'add.html',{'form':form})

class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'sub.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        # bal=int(n1)-int(n2)
        form=OperationForm(request.POST)
        if form .is_valid():
            n1=form.cleaned_data.get('num1')
            n2=form.cleaned_data.get('num2')
            bal=n1-n2
            return render(request,'sub.html',{'balance':bal,'form':form})
        else:
            return render(request,'sub.html',{'form':form})

class MultiplicationView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'multi.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        # pro=int(n1)*int(n2)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get('num1')
            n2=form.cleaned_data.get('num2')
            pro=n1*n2
            return render(request,'multi.html',{'product':pro,'form':form})
        else:
            return render(request,'multi.html',{'form':form})

class DivisionView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'division.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get('num1')
            n2 = form.cleaned_data.get('num2')
            divi=n1/n2
            return render(request,'division.html',{'divis':divi,'form':form})
        else:
            return render(request,'division.html',{'form':form})

class FdivisionView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'floordivision.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        # fdivi=int(n1)//int(n2)
        # return render(request,'division.html',{'fdivis':fdivi})
        form=OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get('num1')
            n2 = form.cleaned_data.get('num2')
            fdivi=n1//n2
            return render(request, 'floordivision.html', {'fdivis': fdivi, 'form': form})
        else:
            return render(request, 'floordivision.html', {'form': form})


class ModulusView(View):
    def get(self,request):
        return render(request,'modulus.html')
    def post(self,request):
        # n1=request.POST.get('num1')
        # n2=request.POST.get('num2')
        # remi=int(n1)%int(n2)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get('num1')
            n2=form.cleaned_data.get('num2')
            remi=n1%n2
            return render(request,'modulus.html',{'reminder':remi,'form':form})
        else:
            return render(request,'modulus.html',{'form':form})

class FactView(View):
    def get(self,request):
        return render(request,'fact.html')
    def post(self,request):
        n1=request.POST.get('num1')
        fact=1
        for i in range(1,int(n1)+1):
            fact=fact*i
        return render(request,'fact.html',{'factorial':fact})

class WordcountView(View):
    def get(self,request):
        return render(request,'wordcount.html')
    def post(self,request):
        text=request.POST.get('word')
        word = text.split(" ")
        wc={}
        for i in word:
            if i in wc:
                wc[i]+=1
            else:
                wc[i]=1
        for k,v in wc.items():
            print(k,v)
        return  render(request,'wordcount.html',{'wordscount':wc})

class PrimeView(View):
    def get(self,request):
        return  render(request,'prime.html')
    def post(self,request):
        l=request.POST.get('llimi')
        u=request.POST.get('ulimi')
        li=[]
        pri={}
        for i in range(int(l),int(u)):
            for j in range(2,i):
                if i%j==0:
                    break
            else:

                li.append(i)
        print(li)
        return render(request,'prime.html',{'result':li})








