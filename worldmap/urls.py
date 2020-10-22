from django.urls import path
from worldmap import views

urlpatterns = [
    path('',views.worldmap,name='worldmap'),
]
