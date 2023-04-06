from django.urls import path
from . import views
app_name='accounts'

urlpatterns = [
    path('signUp/',views.signUP,name='signUp'),
  
]