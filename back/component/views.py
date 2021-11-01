from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.views   import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.
class ComponentView(APIView):
    def get(self, request, format=None):
        type = request.GET['id']
        queryset = Component.objects.filter(data_type=type)
        serializer = ComponentSerializer(queryset, many=True)
        return Response(serializer.data)

class CpuDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Cpu, pk=pk)

    def get(self, request, pk, format=None):
        cpu = self.get_object(pk)
        serializer = CpuSerializer(cpu)
        return Response(serializer.data)

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