from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_medico, name='menu_medico'),  # Menú principal
    path('crear/', views.crear_receta, name='crear_receta'),
    path('listar/', views.listar_recetas, name='listar_recetas'),
    path('editar/<int:id>/', views.editar_receta, name='editar_receta'),
    path('eliminar/<int:id>/', views.eliminar_receta, name='eliminar_receta'),
]