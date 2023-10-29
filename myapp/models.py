from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from slugify import slugify
from django.utils.text import slugify

# Create your models here.




class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    room = models.CharField(max_length=30)
    due_date = models.DateField()
    priority = models.CharField(max_length=30)
    assigned = models.CharField(max_length=30)
    virtual_tour = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)
    project_size = models.CharField(max_length=30)
    project_address= models.CharField(max_length=30)
    add_members = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    project_manager = models.CharField(max_length=30)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.project_name)
            user_slug = slugify(self.user.username)
            unique_slug = f"{base_slug}-{user_slug}"
            i = 1
            while Project.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{user_slug}-{i}"
                i += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.project_name} - Username {self.user.username}'
    
 


class Image(models.Model):
    name = models.CharField(max_length=30, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='360_images/')



class Markup(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    due_date = models.DateField()
    description = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE)  # Assuming you have an Image model
    project = models.ForeignKey('Project', on_delete=models.CASCADE)  # Assuming you have a Project model
    position_x = models.FloatField()  # X-coordinate of the markup on the image
    position_y = models.FloatField()  # Y-coordinate of the markup on the image

    def __str__(self):
        return self.title



# class Image360(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='360_images/')
#     description = models.TextField(blank=True, null=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     date = models.DateField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)