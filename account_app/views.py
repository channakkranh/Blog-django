from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signUP(request):
    form=UserCreationForm,
    # return HttpResponse('hi account')
    # return render (request,'signUp.html',{'form':form}),
