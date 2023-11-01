from django.contrib import admin

from .models import Task
from .models import Project, Image,Markup,Marker

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Markup)
admin.site.register(Marker)
# admin.site.register(Image360)