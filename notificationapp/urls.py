from django.urls import path
from notificationapp import views

urlpatterns =[
    path('',views.notify,name='notify')
]