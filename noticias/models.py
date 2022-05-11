from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.


class Noticia(models.Model):

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    pag_title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField()
    image = models.URLField()
    guid = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return f"{self.title}: {self.description}"
