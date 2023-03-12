from django.db import models
from django.contrib.auth.models import User


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