from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia
# Create your views here.


class HomePageView(ListView):

    template_name = "homepage.html"
    model = Noticia

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.filter().order_by("-pub_date")[:5]
        return context
