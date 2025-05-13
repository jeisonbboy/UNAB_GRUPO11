from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_paciente, name='menu_paciente'),  # Menú principal del módulo Paciente
    path('recetas/', views.visualizar_recetas, name='visualizar_recetas'),  # Visualización de recetas
    path('delivery/', views.solicitar_delivery, name='solicitar_delivery'),  # Solicitud de delivery
    path('seguimiento/', views.seguimiento_pedido, name='seguimiento_pedido'),  # Seguimiento de pedido
]