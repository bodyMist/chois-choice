from rest_framework import serializers
from .models import *

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'

class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'

class MainboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainboard
        fields = '__all__'

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = '__all__'

class HddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hdd
        fields = '__all__'

class SsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ssd
        fields = '__all__'

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = '__all__'

class CoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooler
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'
