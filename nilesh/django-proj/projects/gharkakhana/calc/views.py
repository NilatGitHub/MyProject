from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,'home.html',{'name':'Nilesh'})



def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    result=int(val1)+int(val2)
    return render(request,'result.html',{'result':result})