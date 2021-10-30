from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializer import *
from .models import *

# Create your views here.
class CpuView(viewsets.ModelViewSet):
    serializer_class = CpuSerializer
    queryset = Cpu.objects.all()

class CpuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CpuSerializer
    queryset = Cpu.objects.all()
