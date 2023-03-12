from django.db import models
from coinfind.models import coinfind, finds
from django.contrib.auth.models import User


class coincitjur(models.Model):
    product = models.CharField(max_length=100, verbose_name='Produto Citjur Coin')
    qnt = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.product
    

class buycoincj(models.Model):
    buying = models.ForeignKey(coincitjur, on_delete=models.CASCADE)
    costumerUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário comprador')


    def __str__(self):
        return f'{self.costumerUser} comprou {self.buying}.'
    

    @staticmethod
    def update_coinfind(user, qnt):
        coinfind.objects.filter(userPesquisa=user).update(pesquisas=models.F('pesquisas') + qnt)
        

    def save(self, *args, **kwargs):
        self.qnt = self.buying.qnt 
        self.update_coinfind(self.costumerUser, self.qnt)

    



