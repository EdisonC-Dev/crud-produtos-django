from django.db import models

# definição dos dados de um produto: nome, preço e quantidade em estoque.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome