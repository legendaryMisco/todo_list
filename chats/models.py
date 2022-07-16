from django.contrib.auth.models import User
from django.db import models
from users.models import Register
import uuid
# Create your models here.

class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    sender = models.ForeignKey(Register, on_delete=models.CASCADE,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    receiver_id = models.CharField(max_length=300,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message
