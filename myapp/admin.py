from django.contrib import admin

from .models import Task
from .models import Project, Image,Markup

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Markup)
# admin.site.register(Image360)