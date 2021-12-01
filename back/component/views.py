from rest_framework.views   import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.
class ComponentView(APIView):
    def get(self, request, format=None):
        type = request.GET['id']
        try:
            word = request.GET['word']
            queryset = Component.objects.filter(data_type=type,name__icontains=word)
        except:
            queryset = Component.objects.filter(data_type=type)
        serializer = ComponentSerializer(queryset, many=True)
        return Response(serializer.data)

class CpuListView(APIView):
    def get(self, request, format=None):
        queryset = Cpu.objects.all().only("basic_clock", "max_clock", "socket", "generation")
        serializer = CpuListSerializer(queryset, many=True)
        return Response(serializer.data)

class CpuDetailView(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = Cpu.objects.get(component_component=pk)
        serializer = CpuDetailSerializer(queryset)
        return Response(serializer.data)

class GpuListView(APIView):
    def get(self, request, format=None):
        queryset = Gpu.objects.all().only("memory_type","memory_capacity","required_power")
        serializer = GpuListSerializer(queryset, many=True)
        return Response(serializer.data)
class GpuDetailView(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = Gpu.objects.get(component_component=pk)
        serializer = GpuDetailSerializer(queryset)
        return Response(serializer.data)

class MainboardListView(APIView):
    def get(self, request, format=None):
        queryset = Mainboard.objects.all().only("component_component", "category","chipset_detail",
        "memory_type","memory_speed","memory_channel")
        serializer = MainboardListSerializer(queryset, many=True)
        return Response(serializer.data)
class MainboardDetailView(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = Mainboard.objects.get(component_component=pk)
        serializer = MainboardDetailSerializer(queryset)
        return Response(serializer.data)

class MemoryListView(APIView):
    def get(self, request, format=None):
        queryset=Memory.objects.all().only("type","capacity","clock","timing")
        serializer=MemoryListSerializer(queryset, many=True)
        return Response(serializer.data)
class MemoryDetailView(APIView):
    def get(self,request,format=None):
        pk = request.GET['id']
        queryset = Memory.objects.get(component_component=pk)
        serializer = MainboardDetailSerializer(queryset)
        return Response(serializer.data)

class HddListView(APIView):
    def get(self,request,format=None):
        queryset=Hdd.objects.all().only("size", "capacity","interface")
        serializer=HddListSerializer(queryset, many=True)
        return Response(serializer.data)
class HddDetailView(APIView):
    def get(self,request,format=None):
        pk = request.GET['id']
        queryset = Hdd.objects.get(component_component=pk)
        serializer = HddDetailSerializer(queryset)
        return Response(serializer.data)

class SsdListView(APIView):
    def get(self, request, format=None):
        queryset = Ssd.objects.all().only("forfactor","capacity","interface")
        serializer=SsdListSerializer(queryset, many=True)
        return Response(serializer.data)
class SsdDetailView(APIView):
    def get(self, request, format=None):
        pk=request.GET['id']
        queryset = Ssd.objects.get(component_component=pk)
        serializer=SsdDetailSerializer(queryset)
        return Response(serializer.data)

class PowerListView(APIView):
    def get(self, request, format=None):
        queryset = Power.objects.all().only("type", "certification", "output")
        serializer=PowerListSerializer(queryset, many=True)
        return Response(serializer.data)
class PowerDetailView(APIView):
    def get(self, request, format=None):
        pk=request.GET['id']
        queryset=Power.objects.get(component_component=pk)
        serializer=PowerDetailSerializer(queryset)
        return Response(serializer.data)

class CoolerListView(APIView):
    def get(self,request,format=None):
        queryset=Cooler.objects.all().only("system", "connector", "tdp")
        serializer=CoolerListSerializer(queryset, many=True)
        return Response(serializer.data)
class CoolerDetailView(APIView):
    def get(self,request,format=None):
        pk=request.GET['id']
        queryset=Cooler.objects.get(component_component=pk)
        serializer=CoolerDetailSerializer(queryset)
        return Response(serializer.data)

class CaseListView(APIView):
    def get(self,request,format=None):
        queryset=Case.objects.all().only("type","size","compatibility")
        serializer=CaseListSerializer(queryset)
        return Response(serializer.data)
class CaseDetailView(APIView):
    def get(self, request, format=None):
        pk=request.GET['id']
        queryset=Case.objects.get(component_component=pk)
        serializer=CaseDetailSerializer(queryset)
        return Response(serializer.data)