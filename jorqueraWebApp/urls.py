# URLS DE LA APLICACION

from django.urls import path
from jorqueraWebApp import views    
# from jorqueraWeb.vistas import fun_antecedentes_academicos  otra opcion de importar CLASES
 

urlpatterns = [ 
  # path('home/', fun_home),                                                      # otra forma
    path('home/', views.fun_home),                                                   # pagina 1 
    path('antecedentes_personales/', views.fun_antecedentes_personales),             # pagina 2
    path('antecedentes_academicos/', views.fun_antecedentes_academicos),             # pagina 3 
    path('antecedentes_profesionales/', views.fun_antecedentes_profesionales),       # pagina 4 
    path('contacto/', views.fun_contacto),                                           # pagina 5 
    path('blog/', views.fun_block),                                                 # pagina 5                                       
    
]
