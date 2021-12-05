from rest_framework.views   import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .serializer import *
from .models import *
import time

# Create your views here.
class ComponentView(APIView):
    def get(self, request, format=None):
        type = request.GET['id']
        try:
            word = request.GET['word']
            queryset = cache.get_or_set('component_list',Component.objects.filter(data_type=type,name__icontains=word))
        except:
            queryset = Component.objects.filter(data_type=type)
        serializer = ComponentSerializer(queryset, many=True)
        return Response(serializer.data)

class CpuListView(APIView):
    def get(self, request, format=None):
        #queryset = Cpu.objects.all().only("basic_clock", "max_clock", "socket", "generation")
        queryset = cache.get_or_set('cpu_list',Cpu.objects.all()) 
        serializer = CpuListSerializer(queryset, many=True)
        return Response(serializer.data)

class CpuDetailView(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = cache.get_or_set('cpu_detail_' + pk, Cpu.objects.get(component_component=pk))
        serializer = CpuDetailSerializer(queryset)
        return Response(serializer.data)

class GpuListView(APIView):
    def get(self, request, format=None):
        #queryset = Gpu.objects.all().only("memory_type","memory_capacity","required_power")
        queryset = cache.get_or_set('gpu_list',Gpu.objects.all())
        serializer = GpuListSerializer(queryset, many=True)
        return Response(serializer.data)
class GpuDetailView(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = cache.get_or_set('gpu_detail_' + pk, Gpu.objects.get(component_component=pk))
        serializer = GpuDetailSerializer(queryset)
        return Response(serializer.data)

class MainboardListView(APIView):
    def get(self, request, format=None):
        #queryset = Mainboard.objects.all().only("component_component", "category","chipset_detail",
        #"memory_type","memory_speed","memory_channel")
        queryset = cache.get_or_set('mainboard_list',Mainboard.objects.all())
        serializer = MainboardListSerializer(queryset, many=True)
        return Response(serializer.data)
class MainboardDetailView(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = cache.get_or_set('mainboard_detail_' + pk, Mainboard.objects.get(component_component=pk))
        serializer = MainboardDetailSerializer(queryset)
        return Response(serializer.data)

class MemoryListView(APIView):
    def get(self, request, format=None):
        #queryset=Memory.objects.all().only("type","capacity","clock","timing")
        queryset = cache.get_or_set('memory_list',Memory.objects.all())
        serializer=MemoryListSerializer(queryset, many=True)
        return Response(serializer.data)
class MemoryDetailView(APIView):
    def get(self,request,format=None):
        pk = request.GET['id']
        queryset = cache.get_or_set('memory_datail_' + pk, Memory.objects.get(component_component=pk))
        serializer = MainboardDetailSerializer(queryset)
        return Response(serializer.data)

class HddListView(APIView):
    def get(self,request,format=None):
        #queryset=Hdd.objects.all().only("size", "capacity","interface")
        queryset = cache.get_or_set('hdd_list',Hdd.objects.all())
        serializer=HddListSerializer(queryset, many=True)
        return Response(serializer.data)
class HddDetailView(APIView):
    def get(self,request,format=None):
        pk = request.GET['id']
        queryset = cache.get_or_set('hdd_list_' + pk, Hdd.objects.get(component_component=pk))
        serializer = HddDetailSerializer(queryset)
        return Response(serializer.data)

class SsdListView(APIView):
    def get(self, request, format=None):
        #queryset = Ssd.objects.all().only("forfactor","capacity","interface")
        queryset = cache.get_or_set('ssd_list',Ssd.objects.all())
        serializer=SsdListSerializer(queryset, many=True)
        return Response(serializer.data)
class SsdDetailView(APIView):
    def get(self, request, format=None):
        pk=request.GET['id']
        queryset = cache.get_or_set('ssd_detail_' + pk, Ssd.objects.get(component_component=pk))
        serializer=SsdDetailSerializer(queryset)
        return Response(serializer.data)

class PowerListView(APIView):
    def get(self, request, format=None):
        #queryset = Power.objects.all().only("type", "certification", "output")
        queryset = cache.get_or_set('power_list',Power.objects.all())
        serializer=PowerListSerializer(queryset, many=True)
        return Response(serializer.data)
class PowerDetailView(APIView):
    def get(self, request, format=None):
        pk=request.GET['id']
        queryset = cache.get_or_set('power_detail_' + pk, Power.objects.get(component_component=pk))
        serializer=PowerDetailSerializer(queryset)
        return Response(serializer.data)

class CoolerListView(APIView):
    def get(self,request,format=None):
        #queryset=Cooler.objects.all().only("system", "connector", "tdp")
        queryset = cache.get_or_set('cooler_list',Cooler.objects.all())
        serializer=CoolerListSerializer(queryset, many=True)
        return Response(serializer.data)
class CoolerDetailView(APIView):
    def get(self,request,format=None):
        pk=request.GET['id']
        queryset = cache.get_or_set('cooler_detail_' + pk, Cooler.objects.get(component_component=pk))
        serializer=CoolerDetailSerializer(queryset)
        return Response(serializer.data)

class CaseListView(APIView):
    def get(self,request,format=None):
        #queryset=Case.objects.all().only("type","size","compatibility")
        queryset = cache.get_or_set('case_list', Case.objects.all())
        serializer=CaseListSerializer(queryset)
        return Response(serializer.data)
class CaseDetailView(APIView):
    def get(self, request, format=None):
        pk=request.GET['id']
        queryset = cache.get_or_set('case_detail_' + pk, Case.objects.get(component_component=pk))
        serializer=CaseDetailSerializer(queryset)
        return Response(serializer.data)