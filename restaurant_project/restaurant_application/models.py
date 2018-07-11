from django.db import models

class CategoriaPlatillo(models.Model):
    idCategoriaPlatillo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.categoria)

class Platillo(models.Model):
    codigoPlatillo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precioUnitario = models.DecimalField(max_digits=20, decimal_places=2)
    categoria_platillo = models.ForeignKey(CategoriaPlatillo, null=True, on_delete=models.CASCADE, related_name='platillo')

    def __str__(self):
        return '{}'.format(self.nombre)
