from django import forms
from django.contrib.auth.forms import UserCreationForm



from django import forms
from .models import Task
from .models import Project,Image

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'floor', 'room', 'due_date', 'priority', 'assigned', 'virtual_tour']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','project_size', 'project_address', 'add_members', 'group', 'project_manager', 'date']
    date = forms.DateField(
        )
    




class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image'] 











from django import forms
from django.contrib.auth.forms import AuthenticationForm
