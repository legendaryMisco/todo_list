from django.db import models
import uuid
from users.models import Register
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    time_reminder = models.DateTimeField(editable=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.title