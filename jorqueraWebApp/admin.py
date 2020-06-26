from django.contrib import admin 
from jorqueraWebApp.models import Personas # import la aplicacion y las  o la tablas de mi modelo

# Register your models here.

class Admin (admin.ModelAdmin):
    list_display   =("nombere","edad","apellido_mater","apellido_pater","direccion","email","telefono","comentario")  # muestras als COLUMNAS
    search_fields  =("nombre",)                                # COLUMNA que se buscara
    list_filter    =('nombre','direccion','telefono','email',)                    # filtro en el costado DERECHO
    ordering       =('-telefono',) # orden en que aparezcan als COLUMNAS



# CREA LAS TABLAS EN LE PANEL DE DJANGO
admin.site.register(Personas) 