from django.urls import path
from . import views

urlpatterns = [
    path('acticle-list/',views.acticle_list),
]