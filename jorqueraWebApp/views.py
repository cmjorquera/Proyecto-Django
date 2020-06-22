from django.shortcuts import render

# Create your views here.
#aca van todas las vistas 
#exportar las librerias correspondientes 
##################### IMPORTACIONES IMPORTANTE #####################
from django.shortcuts import render   # para visualizar los HTML
##################### IMPORTACIONES IMPORTANTE #####################


def fun_home (request):                                 # pagina -------->home.html
    return render(request,'home.html')

def fun_contacto (request):                             # pagina -------->Contacto.html
    return render(request,'contacto.html')

def fun_block (request):                                 # pagina -------->block.html
    return render(request,'blog.html')

def fun_antecedentes_profesionales (request):            # pagina -------->ante_profesionales.html
    return render(request,'ante_profesional.html')

def fun_antecedentes_personales(request):                # pagina -------->ante_personales.html
    return render(request,'ante_personales.html')

def fun_antecedentes_academicos(request):                # pagina -------->ante_academicos.html
    return render(request,'ante_academicos.html')
