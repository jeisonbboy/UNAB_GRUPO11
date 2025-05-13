from django.shortcuts import render

# Menú principal del módulo Paciente
def menu_paciente(request):
    return render(request, 'Pacientes/menu_paciente.html')

# Visualización de recetas
def visualizar_recetas(request):
    # Aquí puedes obtener las recetas del paciente desde la base de datos
    recetas = []  # Reemplaza con la consulta real
    return render(request, 'Pacientes/visualizar_recetas.html', {'recetas': recetas})

# Solicitud de delivery
def solicitar_delivery(request):
    if request.method == "POST":
        # Procesa la solicitud de delivery
        pass
    return render(request, 'Pacientes/solicitar_delivery.html')

# Seguimiento de pedido
def seguimiento_pedido(request):
    # Aquí puedes obtener el estado del pedido del paciente
    estado_pedido = "Pendiente"  # Reemplaza con la consulta real
    return render(request, 'Pacientes/seguimiento_pedido.html', {'estado_pedido': estado_pedido})
