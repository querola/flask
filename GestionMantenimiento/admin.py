from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from GestionMantenimiento.models import Tecnicos
# Register your models here.
from GestionMantenimiento.models import DTCEncabezado,CatalogoPlace,CatalogoCarril,DTCTecnico,UsuarioPlaza,Tecnicos, CatalagoComponentes

#admin.site.register(DTCEncabezado)
@admin.register(DTCEncabezado)
class DTCEncabezado(admin.ModelAdmin):
    list_display = ('NoConvenio', 'NombreEncargado' , 'Cargo')
    list_editable = ('NombreEncargado' , 'Cargo')
#admin.site.register(CatalogoPlace)
@admin.register(CatalogoPlace)
class CatalogoPlace(admin.ModelAdmin):
    list_display = ('NoPlazaCapufe', 'Place', 'Delegacion')
    list_editable = ('Place' , 'Delegacion')
#admin.site.register(CatalogoCarril)
@admin.register(CatalogoCarril)
class CatalogoCarril(admin.ModelAdmin):
    list_display = ('NoCapufeLane', 'Lane' , 'TypeLane')
    list_editable = ('Lane' , 'TypeLane')
#admin.site.register(DTCTecnico)
@admin.register(DTCTecnico)
class DTCTecnico(admin.ModelAdmin):
    search_fields = ('NoAXA', 'FolioFalla', 'NoReference')
    list_display = ('FolioFalla', 'NoReference', 'NoAXA')
    #se me muestran conforme esten acomodados
    list_filter = ('FolioFalla', 'NoReference')
@admin.register(UsuarioPlaza)
class UsuarioPlaza(admin.ModelAdmin):
    list_display = ('idusuario','noplazacapufe')

    #vuelve links los datos
    #list_display_links = ('user'.'phone_Number')
    #vuelve editable los campos desde la vista no pueden ser tambien links
    #list_editable = ('')
    #Acomoda las columas
    #fieldsets

# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Tecnicos
    can_delete = False
    verbose_name_plural = 'Tecnicos'
@admin.register(CatalagoComponentes)
class CatalagoComponentes(admin.ModelAdmin):
    list_display = ('NoPart','DescriptionComponent')

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


