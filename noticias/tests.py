from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
# Create your tests here.

from .models import Noticia


class NoticiasTest(TestCase):

    def setUp(self) -> None:
        self.noticia = Noticia.objects.create(
            title="noticia de ultima hora",
            category="Manga",
            description="Segunda temporada comfirmada",
            pub_date=timezone.now(),
            image=r"https://mi_image.com",
            guid="pb123456",
            link="https://mi_pagina.com"
        )

    def test_atributes(self):
        self.assertEqual(self.noticia.title, "noticia de ultima hora")
        self.assertEqual(self.noticia.description, "Segunda temporada comfirmada")
        self.assertEqual(self.noticia.guid, "pb123456")
        self.assertEqual(self.noticia.category, "Manga")

    def test_str_representation(self):
        self.assertEqual(
            str(self.noticia),
            "noticia de ultima hora: Segunda temporada comfirmada"
        )

    def test_homepage_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_list_content(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "noticia de ultima hora")
