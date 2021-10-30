from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MemberView.as_view({'get': 'list'})),
    path('<int:pk>/', views.DetailMember.as_view()),
]