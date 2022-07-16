from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Register


def createAccount(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile = Register.objects.create(
            user=user,
            username=user.username,
            fullname=user.first_name,
            email=user.email
        )

def updateAccount(sender,instance,created,**kwargs):
    register = instance
    user = register.user
    if created == False:
        user.first_name = register.fullname
        user.username = register.username
        user.email = register.email
        user.save()


def deleteAccount(sender,instance,**kwargs):
    user=instance.user
    user.delete()

post_save.connect(createAccount, sender=User)
post_save.connect(updateAccount, sender=Register)
post_delete.connect(deleteAccount, sender=Register)

































