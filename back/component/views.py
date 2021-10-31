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


# Create your views here.
class GpuView(viewsets.ModelViewSet):
    serializer_class = GpuSerializer
    queryset = Gpu.objects.all()

class GpuDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GpuSerializer
    queryset = Gpu.objects.all()

    
# Create your views here.
class SsdView(viewsets.ModelViewSet):
    serializer_class = SsdSerializer
    queryset = Ssd.objects.all()

class SsdDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SsdSerializer
    queryset = Ssd.objects.all()
    

# Create your views here.
class MainboardView(viewsets.ModelViewSet):
    serializer_class = MainboardSerializer
    queryset = Mainboard.objects.all()

class MainboardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MainboardSerializer
    queryset = Mainboard.objects.all()
    

# Create your views here.
class MemoryView(viewsets.ModelViewSet):
    serializer_class = MemorySerializer
    queryset = Memory.objects.all()

class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemorySerializer
    queryset = Memory.objects.all()


# Create your views here.
class HddView(viewsets.ModelViewSet):
    serializer_class = HddSerializer
    queryset = Hdd.objects.all()

class HddDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HddSerializer
    queryset = Hdd.objects.all()

    
# Create your views here.
class PowerView(viewsets.ModelViewSet):
    serializer_class = PowerSerializer
    queryset = Power.objects.all()

class PowerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PowerSerializer
    queryset = Power.objects.all()

    
# Create your views here.
class CoolerView(viewsets.ModelViewSet):
    serializer_class = CoolerSerializer
    queryset = Cooler.objects.all()

class CoolerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoolerSerializer
    queryset = Cooler.objects.all()

    
# Create your views here.
class CaseView(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()

class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()