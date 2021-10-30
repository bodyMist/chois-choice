from django.contrib import admin

from .models import Component, Case, Cooler, Cpu, Gpu, Hdd, Mainboard, Memory, Power, Ssd

# Register your models here.
admin.site.register(Component)
admin.site.register(Cpu)
admin.site.register(Gpu)
admin.site.register(Mainboard)
admin.site.register(Memory)
admin.site.register(Hdd)
admin.site.register(Ssd)
admin.site.register(Power)
admin.site.register(Cooler)
admin.site.register(Case)
