
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Acticle

# def home(request):
#     # return HttpResponse ('hello homepage')
#     return render(request,'homepage.html')

# def about(request):
#     # return HttpResponse('hello aboutpage')
#     return render (request,'aboutpage.html')

def acticle_list(request):
    # return HttpResponse('acticles_list')
    acticles=Acticle.objects.all().order_by('date')
    return render(request,'acticles/acticle_list.html',{'acticles':acticles})