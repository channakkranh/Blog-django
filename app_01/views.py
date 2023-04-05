from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse ('hello homepage')
    return render(request,'homepage.html')

def about(request):
    # return HttpResponse('hello aboutpage')
    return render (request,'aboutpage.html')

 