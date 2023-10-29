from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect , get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required



from django.http import HttpResponse

from .forms import TaskForm
from .forms import ProjectForm
from .models import Image, Task
from .models import Project


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the logged-in user
            task.save()
            return redirect('tasks')  # Redirect to a page displaying the task list
    else:
        form = TaskForm()


    # tasks = Task.objects.filter(user=request.user)
    # tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    # tasks = Task.objects.filter(user=request.user).order_by('-id')
    # tasks = Task.objects.filter(user=request.user).order_by('-created_at') # Order by created_at in descending order
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    

    return render(request, 'create_task.html', {'form': form, 'tasks': tasks})




def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            
            if Project.objects.filter(project_name=project.project_name, user=project.user).exists():
                form.add_error('project_name', 'A project with this name already exists.')
            else:
                project.save()
                return redirect('virtual')
    else:
        form = ProjectForm()
    projects = Project.objects.filter(user=request.user).order_by('created_at')
    # projects = Project.objects.all().order_by('-created_at')
    # projects = Project.objects.order_by('created_at')

    return render(request, 'create_project.html', {'form': form, 'projects': projects})


def edit_project(request, project_slug):
    # Get the project object based on the project_slug
    project = get_object_or_404(Project, slug=project_slug, user=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('virtual')

    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})


def virtual_tour(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    if request.method == 'POST':
        
        image = request.FILES['360_image']
        Image.objects.create(project=project, image=image)

    images = Image.objects.filter(project=project)
    return render(request, 'virtual_tour.html', {'project': project, 'images': images})










@login_required
def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    images = Image.objects.filter(project=project)
    return render(request, 'project_detail.html', {'project': project, 'images': images})


@login_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)

        # Check if the user is the owner of the task
        if task.user != request.user:
            raise Http404("Task not found")
        
        task.delete()
        
    except Task.DoesNotExist:
        raise Http404("Task not found")
    
    return redirect('tasks')






def landing_page(request):
    return render(request, 'index.html')



@login_required
def tasks_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    task_count = Task.objects.filter(user=request.user).count()
    return render(request, 'task.html', {'tasks': tasks, 'task_count': task_count, 'projects': projects})
















def virtual_view(request):
    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    project_count = Project.objects.filter(user=request.user).count()
    task_count = Task.objects.filter(user=request.user).count()

    return render(request, 'virtual.html', {'project_count': project_count, 'projects' : projects, 'task_count': task_count})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Replace 'index' with your landing page URL
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  # Replace 'index' with your landing page URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')  # Replace 'index' with your landing page URL


@login_required
def dash(request):
    task_count = Task.objects.filter(user=request.user).count()
    # projects = Project.objects.all().order_by('-created_at')
    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    
    
    return render(request, 'over.html', {'task_count': task_count, 'projects': projects})  # Replace 'dashboard.html' with your actual dashboard template



