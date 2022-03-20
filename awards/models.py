from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
# project models
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_image = models.ImageField(upload_to = 'media/', null = True, blank = True)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=150, default="Nairobi")
  
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    # update project
    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    avg_rate = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        rating = Rating.objects.filter(id=id).first()
        return rating

    def __str__(self):
        return self.user.username


