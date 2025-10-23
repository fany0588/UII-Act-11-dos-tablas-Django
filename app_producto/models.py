from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200, help_text="Nombre del producto")
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    # Categoria ahora es un CharField, no una ForeignKey a un modelo separado
    categoria = models.CharField(max_length=100, blank=True, null=True, 
    help_text="Categoría del producto (ej. Helado, Agua, Postre)")
    foto = models.ImageField(upload_to='img_productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=200, unique=True)
    contacto = models.CharField(max_length=100, blank=True, null=True, help_text="Nombre de la persona de contacto")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tipo_producto = models.CharField(max_length=100, blank=True, null=True, help_text="Tipo de productos que suministra")
    
    productos = models.ManyToManyField(Producto, related_name='proveedores', blank=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre_empresa']