from django.db import models
from django.core.urlresolvers import reverse

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
                        choices= UNIDAD_DE_MEDIDA_CHOICES,
                        default = UNIDADES,
                        max_length=30
                    )
    
    def __str__(self):
        return '{} - {}'.format(self.id , self.nombre)

class ReporteDeExistencia(models.Model):
    fecha_reporte = models.DateField()
    observaciones = models.TextField(max_length=512, blank=True)
    class Meta():
        ordering = ['fecha_reporte']

    def __str__(self):
        return 'Reporte de existencias a fecha {}'.format(self.fecha_reporte)
    def get_absolute_url(self):
        return reverse("inventario:reporte_detail", kwargs={'pk':self.pk})

class Existencia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    reporte_de_existencia = models.ForeignKey(ReporteDeExistencia, on_delete=models.CASCADE, related_name='existencias', default=None)
    existencias = models.PositiveIntegerField()
    
    def __str__(self):
        unidad_de_medida_producto = ''
        for unidad_de_medida in Producto.UNIDAD_DE_MEDIDA_CHOICES:
            if(unidad_de_medida[0] == self.producto.unidad_de_medida):
                unidad_de_medida_producto = unidad_de_medida[1]
        return 'Códido: {} - Descripción: {} - Cantidad: {} - Unidad: {} - Fecha: {}'.format(self.producto.id, self.producto.nombre, self.existencias, unidad_de_medida_producto, self.reporte_de_existencia.fecha_reporte)

