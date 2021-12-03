from django.db.models import fields
from rest_framework import serializers
from .models import *

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class CpuDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Cpu
        fields = '__all__'
class CpuListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Cpu
        #fields = ("component_component","basic_clock", "max_clock","socket", "generation")
        fields = '__all__'

class GpuDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Gpu
        fields = '__all__'
class GpuListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Gpu
        #fields = ("component_component","memory_type","memory_capacity","required_power")    
        fields = '__all__'

class MainboardDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Mainboard
        fields = '__all__'
class MainboardListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Mainboard
        #fields = ("component_component", "category","chipset_detail",
        #"memory_type","memory_speed","memory_channel")
        fields = '__all__'

class MemoryDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Memory
        fields = '__all__'
class MemoryListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Memory
        #fields = ("type","capacity","clock","timing")
        fields = '__all__'

class HddDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Hdd
        fields = '__all__'
class HddListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Hdd
        #fields = ("size", "capacity","interface")
        fields = '__all__'

class SsdDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Ssd
        fields = '__all__'
class SsdListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Ssd
        #fields = ("forfactor","capacity","interface")
        fields = '__all__'

class PowerDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Power
        fields = '__all__'
class PowerListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Power
        #fields = ("type", "certification", "output")
        fields = '__all__'

class CoolerDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Cooler
        fields = '__all__'
class CoolerListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Cooler
        #fields = ("system", "connector", "tdp")
        fields = '__all__'

class CaseDetailSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Case
        fields = '__all__'
class CaseListSerializer(serializers.ModelSerializer):
    component_component = ComponentSerializer(required=True)
    class Meta:
        model = Case
        #fields = ("type","size","compatibility")
        fields = '__all__'