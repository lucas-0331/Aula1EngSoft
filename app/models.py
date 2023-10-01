from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome
    
class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length = 50)
    categoria = models.ForeignKey(Categoria,
                                  on_delete = models.CASCADE)
    marca = models.ForeignKey(Marca,
                              on_delete=models.CASCADE)
    preco = models.PositiveIntegerField()
    quantidade = models.IntegerField()
    disponivel = models.BooleanField()
    data = models.DateTimeField()

    def __str__(self):
        return f'{self.categoria} {self.marca} {self.nome}'