from django.db import models
from blog.models import BlogIndexPage
from peliculas.models import CochesIndexPage
from peliculas.models import PelisIndexPage

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
    subpage_types = ['blog.BlogIndexPage','peliculas.PelisIndexPage','peliculas.CochesIndexPage', 'centros.CentrosIndexPage']