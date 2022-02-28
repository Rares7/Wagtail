from pyexpat import model
from django.db import models
from django import forms

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your models here.

## Page que mostrará el index de las películas
## Hereda solo de Home y no descendientes

## Modelo para películas

class Coche(models.Model):
    iden = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=60)
    
    panels = [
        FieldPanel('iden'),
        FieldPanel('marca'),
        FieldPanel('modelo'),
    ]
    def __str__(self):
        return f'{self.marca} {self.modelo}'   

class Pelicula(models.Model):
    title = models.CharField('título', max_length=250)
    #slug = models.SlugField()
    rating = models.DecimalField(max_digits=6, decimal_places=4)
    link = models.URLField()
    place = models.IntegerField()
    year = models.IntegerField()
    imagen = models.URLField()
    cast = models.CharField(max_length = 250, 
        help_text='Introduzca nombres separados por comas')

    panels = [
        FieldPanel('title'),
        FieldPanel('rating'),
        FieldPanel('link'),
        FieldPanel('place'),
        FieldPanel('year'),
        FieldPanel('imagen'),
        FieldPanel('cast')
    ]
    def __str__(self):
        return f'{self.title} ({self.year})'
    
class PeliculaPage(Page):
    """
    Detail view for a specific bread
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    
class PelisIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['peliculas'] = Pelicula.objects.all()
        
        return context
    

    def get_peliculas(self):
        return PeliculaPage.objects.live().descendant_of(
            self).order_by('first_published_at')

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_peliculas(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages