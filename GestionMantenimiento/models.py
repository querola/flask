from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class DTCEncabezado(models.Model):
    id = models.IntegerField(primary_key=True)
    NoConvenio = models.IntegerField(unique=True)
    NombreEncargado = models.CharField(max_length=50)
    Cargo = models.CharField(max_length=100)

class Tecnicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone_Number = models.CharField(_('Numero De Telefono: '),max_length=10)
    rol_Usuario = models.CharField(_('Tipo de usuario'),max_length=20)
    def __str__(self):
        """Return Username"""
        return self.user.username

class CatalogoPlace(models.Model):
    NoPlazaCapufe = models.IntegerField(_('No. Plaza Capufe:'),primary_key=True)
    Place = models.CharField(_('Nombre:'),max_length=30)
    Delegacion = models.CharField(_('Delegación:'),max_length=30)

    def __str__(self):
        """Return Username"""
        #return 'el nombre de la 
        return self.Place


class CatalogoCarril(models.Model):
    NoCapufeLane = models.IntegerField(_('No. Capufe'),primary_key=True,unique=True)
    Lane = models.CharField(_('Carril'),max_length=3,help_text=_(''))
    TypeLane = models.CharField(_('Tipo De Carril'), max_length=15)
    noplazacapufe = models.ForeignKey(CatalogoPlace, on_delete=models.CASCADE)
    def __str__(self):
        """Return Username"""
        #return 'el nombre de la 
        return self.noplazacapufe.Place

class CatalagoComponentes(models.Model):
    NoPart = models.CharField(_('No. De Parte'),primary_key=True,unique=True, max_length=50)   
    DescriptionComponent = models.TextField(_('Descripcion del componente'))
    Price = models.IntegerField(_('Costo'))
    unity = models.CharField(_('Unidad'), max_length=50)
    TypeService = models.CharField(max_length=50)
    YearPrice = models.DateField(_('Año'))
    Brand =  models.CharField(_('Marca del componente'), max_length=50)
    ImageDescription = models.ImageField(
        upload_to='Componentes/pictures',
        blank=True,
        null=True
    )
    def __str__(self):
        """Return Username"""
        #return 'el nombre de la 
        #cadena = self.catalogocarril.Lane + 
        return self.DescriptionComponent

class DTCTecnico(models.Model):
    NoReference = models.CharField(max_length=12, primary_key=True)
    catalogocarril = models.ForeignKey(CatalogoCarril , on_delete=models.CASCADE)
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    catalagocomponentes = models.ForeignKey(CatalagoComponentes, on_delete=models.CASCADE)
    NoAXA = models.CharField(max_length=8,unique=True)
    FolioFalla = models.IntegerField(unique=True)
    Estatus = models.CharField(max_length=30)
    DateFalla = models.DateField()
    DateSiniestro = models.DateField()
    DateElaboracion = models.DateField()
    DateEnvio = models.DateField()
    TypeDictamen = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    Diagnostic = models.TextField(blank=True)
    Observation = models.TextField(blank=True )
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    def __str__(self):
        """Return Username"""
        #return 'el nombre de la 
        #cadena = self.catalogocarril.Lane + 
        return self.catalagocomponentes.NoPart

class UsuarioPlaza(models.Model):
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    noplazacapufe = models.ForeignKey(CatalogoPlace, on_delete=models.CASCADE)
    def __str__(self):
        """Return Username"""
        return self.noplazacapufe.Place


# Create your models here.
