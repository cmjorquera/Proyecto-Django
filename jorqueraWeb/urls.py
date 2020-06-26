"""jorqueraWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include     # include para incluir las urls de APP


##################### IMPORTACIONES IMPORTANTE #####################

#from jorqueraWeb.vistas import fun_home,fun_contacto,fun_antecedentes_academicos,fun_antecedentes_personales,
# fun_antecedentes_profesionales,fun_block,fun_contacto                          # otra forma
# from jorqueraWeb import vistas                                                   # importar las clase VISTAS.PY
##################### IMPORTACIONES IMPORTANTE #####################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('jorqueraWebApp.urls'),)             # incluyo las url de mi APP a ocupar "jorqueraWebApp"
    # path('home/', fun_home),                                                        # otra forma
    # path('home/', vistas.fun_home),                                                   # pagina 1 
    # path('antecedentes_personales/', vistas.fun_antecedentes_personales),             # pagina 2
    # path('antecedentes_academicos/', vistas.fun_antecedentes_academicos),             # pagina 3 
    # path('antecedentes_profesionales/', vistas.fun_antecedentes_profesionales),       # pagina 4 
    # path('contacto/', vistas.fun_contacto),                                           # pagina 5 
    # path('block/', vistas.fun_block),                                                 # pagina 6 
    
]
