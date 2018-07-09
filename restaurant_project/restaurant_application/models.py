from django.db import models

class CategoriaPlatillo(models.Model):
    idCategoriaPlatillo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=200)
