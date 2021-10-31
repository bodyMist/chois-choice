from django.shortcuts import render
from rest_framework import generics
from rest_framework.views   import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.
class ComponentView(APIView):
    def get(self, request, format=None):
        type = request.GET['type']
        queryset = Component.objects.filter(data_type=type)
        serializer = ComponentSerializer(queryset, many=True)
        return Response(serializer.data)

class CpuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CpuSerializer
    queryset = Cpu.objects.all()

class GpuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GpuSerializer
    queryset = Gpu.objects.all()

class SsdDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SsdSerializer
    queryset = Ssd.objects.all()

class MainboardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MainboardSerializer
    queryset = Mainboard.objects.all()

class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemorySerializer
    queryset = Memory.objects.all()

class HddDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HddSerializer
    queryset = Hdd.objects.all()

class PowerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PowerSerializer
    queryset = Power.objects.all()

class CoolerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoolerSerializer
    queryset = Cooler.objects.all()

class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()