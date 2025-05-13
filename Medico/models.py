from django.db import models

class Receta(models.Model):
    paciente = models.CharField(max_length=100)  # Nombre del paciente
    medicamentos = models.TextField()  # Lista de medicamentos
    dosis = models.TextField()  # Dosis de los medicamentos
    observaciones = models.TextField(blank=True, null=True)  # Observaciones opcionales
    fecha_emision = models.DateTimeField(auto_now_add=True)  # Fecha de emisión
    estado = models.CharField(max_length=20, default="Pendiente")  # Estado de la receta

    def __str__(self):
        return f"Receta para {self.paciente} - {self.fecha_emision}"
