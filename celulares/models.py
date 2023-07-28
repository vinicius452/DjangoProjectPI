from django.db import models


class Celular(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    data_lancamento = models.DateField()
    foto = models.ImageField(upload_to='celulares/', default='default.webp')

    def __str__(self):
        return f"{self.marca} {self.modelo}"
