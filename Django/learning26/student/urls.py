from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.studenthome),
    path("study/",views.studentlist),
    

]