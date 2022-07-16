from django.db import models

from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Register(models.Model):
    fullname = models.CharField(max_length=300,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    phonenumber = models.IntegerField(null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=400,null=True,blank=True)
    profile_image = models.ImageField(max_length=3000,null=True,blank=True,upload_to='profile_image/',default='user-default.png')
    short_intro = models.CharField(max_length=300,null=True,blank=True,default="i am a new user")
    bio = models.TextField(null=True,blank=True, default='i am a new user')

    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.username
