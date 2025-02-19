from django.shortcuts import render

def prueba(request):
    return render(request, 'index.html')  # Ruta correcta de la plantilla

