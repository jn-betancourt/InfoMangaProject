from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia
# Create your views here.


class HomePageView(ListView):

    template_name = "homepage.html"
    model = Noticia

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.filter().order_by("-pub_date")
        return context


class AnimePageView(ListView):

    template_name = "anime.html"
    model = Noticia

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.filter().order_by("-pub_date")
        return context


class MangaPageView(ListView):

    template_name = "manga.html"
    model = Noticia

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.filter().order_by("-pub_date")
        return context
