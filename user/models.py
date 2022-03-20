from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=250, blank=True, null=True)
    contact = models.CharField(max_length=250, blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        
    def update(self):
        self.save()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile
        
    
    

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
    