from re import S
from django.contrib import admin
from .models import Servicio, Empresa, Distrito
# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display=("id","nombre","created","updated")
    search_fields=("id","nombre")

class ServicioAdmin(admin.ModelAdmin):
    list_display=("id","titulo","Contenido","empresa_id","created","updated")
    search_fields=("id","titulo")
    list_filter=("empresa_id",)

class DistritoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","av_principal","servicio_id","created","updated")
    search_fields=("id","nombre")
    list_filter=("nombre",)
    
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Distrito, DistritoAdmin)