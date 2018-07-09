from django.db import models


class Producto(models.Model):
    KILOGRAMOS = 'kg'
    LIBRAS = 'lbl'
    TONELADAS_LARGAS = 'tnl'
    TONELADAS_METRICAS = 'tnm'
    TONELADAS_CORTAS = 'tnc'
    GRAMOS = 'g'
    UNIDADES = 'u'
    LITROS = 'lt'
    GALONES = 'gal'
    BARRILES = 'bar'
    LATAS = 'lts'
    CAJAS = 'caj'
    MILLARES = 'mil'
    METROS_CUBICOS = 'm3'
    METROS = 'm'
    OTROS = 'o'
    UNIDAD_DE_MEDIDA_CHOICES = (
        (KILOGRAMOS,'Kilogramos'),
        (LIBRAS, 'Libras'),
        (TONELADAS_LARGAS, 'Toneladas Largas'),
        (TONELADAS_METRICAS, 'Toneladas Metricas'),
        (TONELADAS_CORTAS, 'Toneladas Cortas'),
        (GRAMOS, 'Gramos'),
        (UNIDADES, 'Unidades'),
        (LITROS, 'Litros'),
        (GALONES, 'Galones'),
        (BARRILES, 'Barriles'),
        (LATAS, 'Latas'),
        (CAJAS, 'Cajas'),
        (MILLARES, 'Millares'),
        (METROS_CUBICOS, 'Metros cúbicos'),
        (METROS, 'Metros'),
        (OTROS, 'Otros'),
    )
    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(
                        max_length=3,
                        choices= UNIDAD_DE_MEDIDA_CHOICES,
                        default = UNIDADES
                    )
    
    def __str__(self):
        return self.nombre

class Existencia(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='producto')
    fecha_existencia = models.DateField(auto_now=True)
    existencias = models.PositiveIntegerField()