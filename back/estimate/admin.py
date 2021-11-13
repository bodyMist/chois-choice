from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Estimation)
admin.site.register(Evaluations)
admin.site.register(EstimationHasComponent)
admin.site.register(Annotations)
admin.site.register(Uses)