from django.urls import path
from . import views

app_name = 'app_producto' # Cambiamos el nombre de la aplicación a 'app_producto'

urlpatterns = [
    # --- URLs para Productos ---
    path('', views.listar_productos, name='listar_productos'), # Ruta raíz para listar productos
    path('productos/', views.listar_productos, name='listar_productos_alt'), # Otra ruta opcional para listar productos
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]