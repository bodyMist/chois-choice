from django.urls import path
from .views import *

urlpattern = [
    path('cpu/', CpuView.as_view({'get': 'list'})),
    path('cpu/<int:pk>/', CpuDetail.as_view()),
]