from django.contrib import admin

from .models import Task
from .models import Project, Image,Marker,FloorPlan, Hotspot

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(FloorPlan)
admin.site.register(Hotspot)

admin.site.register(Marker)
# admin.site.register(Image360)