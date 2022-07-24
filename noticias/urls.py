from django.urls import path
from .views import HomePageView, AnimePageView, MangaPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("anime", AnimePageView.as_view(), name="animepage"),
    path("manga", MangaPageView.as_view(), name="mangapage"),
]
