from django.shortcuts import render

def menu_productos(request):
    return render(request, 'Productos/menu_productos.html')

def gestion_productos(request):
    return render(request, 'Productos/gestion_productos.html')

def edicion_productos(request):
    # Aquí puedes obtener el producto a editar desde la base de datos
    producto = {
        'codigo': '123456',
        'descripcion': 'Producto de ejemplo',
        'marca': 'Marca Ejemplo',
        'lote': 'Lote123',
        'fecha_vencimiento': '2025-12-31',
        'precio_lista': 100.00,
        'stock_disponible': 50,
        'unidad_medida': 'ml',
        'requiere_receta': True,
        'observaciones': 'Sin observaciones',
    }
    return render(request, 'Productos/edicionProductos.html', {'productos': producto})
