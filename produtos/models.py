from django.db import models


class Produto(models.Model):

    CATEGORIAS = [
        ("perifericos", "Periféricos"),
        ("hardware", "Hardware"),
        ("monitores", "Monitores"),
        ("acessorios", "Acessórios"),
        ("outros", "Outros"),
    ]

    nome = models.CharField(max_length=100)

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque = models.IntegerField()

    categoria = models.CharField(
        max_length=100,
        choices=CATEGORIAS,
        default="outros"
    )

    def __str__(self):
        return self.nome