from django.urls import path
from testcorona import views
urlpatterns = [
    path('report',views.report,name="report"),
    path('',views.testcorona,name="testcorona"),
    
]

