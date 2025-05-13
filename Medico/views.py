from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta

def menu_medico(request):
    return render(request, 'Medico/menu_medico.html')

# Crear receta
def crear_receta(request):
    if request.method == "POST":
        paciente = request.POST['paciente']
        medicamentos = request.POST['medicamentos']
        dosis = request.POST['dosis']
        observaciones = request.POST.get('observaciones', '')

        Receta.objects.create(
            paciente=paciente,
            medicamentos=medicamentos,
            dosis=dosis,
            observaciones=observaciones
        )
        return redirect('listar_recetas')
    return render(request, 'Medico/crear_receta.html')

# Listar recetas
def listar_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_emision')
    return render(request, 'Medico/listar_recetas.html', {'recetas': recetas})

# Editar receta
def editar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    if request.method == "POST":
        receta.paciente = request.POST['paciente']
        receta.medicamentos = request.POST['medicamentos']
        receta.dosis = request.POST['dosis']
        receta.observaciones = request.POST.get('observaciones', '')
        receta.save()
        return redirect('listar_recetas')
    return render(request, 'Medico/editar_receta.html', {'receta': receta})

# Eliminar receta
def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    if receta.estado == "Pendiente":
        receta.delete()
    return redirect('listar_recetas')
