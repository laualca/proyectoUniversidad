from django.shortcuts import render

# Create your views here.
def formularioContacto(request):
    return render(request, 'formularioContacto.html')