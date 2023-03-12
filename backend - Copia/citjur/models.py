from django.db import models


class Questions(models.Model):
    pergunta = models.CharField(max_length=150)
    respondida = models.BooleanField(default=False)

    def __str__(self):
        return self.pergunta
    

class Answer(models.Model):
    resposta = models.TextField()
    perguntaResp = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.resposta
