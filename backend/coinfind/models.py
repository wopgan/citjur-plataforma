from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = super().create_user(email, password=password, **extra_fields)
        coinfind.objects.create(userPesquisa=user, pesquisas=3)
        return user


class coinfind(models.Model):
    pesquisas = models.CharField(max_length=10)
    userPesquisa = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.userPesquisa} tem {self.pesquisas} pesquisas' 
    
   

class finds(models.Model):
    research_done = models.CharField(max_length=10)
    userPesquisa = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):    
        if self.pk is None: 
            coinfind.objects.filter(userPesquisa=self.userPesquisa).update(pesquisas=models.F('pesquisas')-1)
        super().save(*args, **kwargs)


@receiver(user_signed_up)
def create_coinfind(sender, **kwargs):
    user = kwargs['user']
    coinfind.objects.create(userPesquisa=user, pesquisas=3)


User._default_manager.__class__ = CustomUserManager