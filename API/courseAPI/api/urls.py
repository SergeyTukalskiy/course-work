from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('students/', views.getStudents),
    path('login/', views.auth),
    path('student/', views.getStudentInfo),
    path('step/', views.setStep),

]