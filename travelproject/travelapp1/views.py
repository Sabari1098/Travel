from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import meet

def demo(request):
     obj=place.objects.all()
     obj1=meet.objects.all()
     return render(request,'index.html',{'result':obj,'result1':obj1})
# def operator(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res=x+y
#      sub=x-y
#      mul=x*y
#      div=x/y
#      return render(request,'result.html',{'result':res,'subst':sub,'multi':mul,'divis':div})
