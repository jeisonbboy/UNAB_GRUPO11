from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_productos, name='menu_productos'),  # Menú principal de Productos
    path('gestion/', views.gestion_productos, name='gestion_productos'),  # Gestión de Productos
    path('edicion/', views.edicion_productos, name='edicion_productos'),  # Edición de Productos
]