
from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
    path('createEmployeeWithForm/',views.createEmployeeWithForm),
    path('createCourse/',views.createCourse),
    path('createTeacher/',views.createTeacher),
    path('createProduct/',views.createProduct),
    path('createStudent/',views.createStudent)
]