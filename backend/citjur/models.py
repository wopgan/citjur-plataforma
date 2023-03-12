from django.db import models
from coinfind.models import coinfind
from django.contrib.auth.models import User


class Questions(models.Model):
    pergunta = models.CharField(max_length=150)
    respondida = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.pergunta
    

class Answer(models.Model):
    resposta = models.TextField()
    perguntaResp = models.ForeignKey(Questions, on_delete=models.CASCADE)


    def __str__(self):
        return self.resposta
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        coinfind.objects.filter(userPesquisa=self.perguntaResp.user).update(pesquisas=models.F('pesquisas') - 1)
