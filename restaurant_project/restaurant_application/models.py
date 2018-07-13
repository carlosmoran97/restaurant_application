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

class Mesa(models.Model):
    codigo_mesa = models.AutoField(primary_key=True)
    numero_mesa = models.IntegerField()
    asientos = models.IntegerField()
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.numero_mesa)

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    dui = models.CharField(max_length=9)
    nit = models.CharField(max_length=14)
    afp = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)

class Puesto(models.Model):
    idPuesto = models.AutoField(primary_key=True)
    puesto = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.puesto)

class Asignacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='asignacion_empleado')
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, related_name='asignacion_puesto')
    salario = models.DecimalField(max_digits=20, decimal_places=2)
    fecha_contratacion = models.DateField()

    class Meta:
        unique_together = ('empleado', 'puesto')
