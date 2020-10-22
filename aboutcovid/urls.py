from django.urls import path
from django.shortcuts import render
from aboutcovid import views

urlpatterns = [
    path("",views.aboutcovid,name="aboutcovid")
]
