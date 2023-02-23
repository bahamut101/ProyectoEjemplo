from django.contrib import admin

# Register your models here.

from gestionCursos.models import Cursos, Alumnos, Pedidos

class PedidosAdmin(admin.ModelAdmin):
    list_display=('ref','fecha','finalizado')
    search_fields=('fecha','ref')

class FiltroAlumnos(admin.ModelAdmin):
    list_filter=('nombre',)


admin.site.register(Cursos)
admin.site.register(Alumnos, FiltroAlumnos)
admin.site.register(Pedidos, PedidosAdmin)