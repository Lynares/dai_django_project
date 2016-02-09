from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Bares(models.Model):
    id_bar = models.AutoField(primary_key=True)
    n_bar = models.CharField(max_length=128, unique=True)
    direccion = models.CharField(max_length=128, unique=True)
    visitas = models.IntegerField(default=10)
    slug = models.SlugField() 

    def save(self, *args, **kwargs): 
    	self.slug = slugify(self.n_bar) 
    	super(Bares, self).save(*args, **kwargs)

    def __unicode__(self):  
        return self.n_bar

class Tapas(models.Model):
    n_bar = models.ForeignKey(Bares)
    id_tapa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    votos = models.IntegerField(default=0)

    def __unicode__(self): 
        return self.nombre

#class UserProfile(models.Model):
    #Esta linea es requerida para linkar UserProfile con una instancia de User model, que nos proporciona Django
#    user = models.OneToOneField(User)

    #Atributos adicionales
#    website = models.URLField(blank=True)
#    picture = models.ImageField(upload_to='profile_images', blank=True)

    #Override __unicode__() para devolver algo significativo
 #   def __unicode__(self):
 #       return self.user.username
        