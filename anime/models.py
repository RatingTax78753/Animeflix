from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


TIPO_EPISODIO = (
    ('Abertura', 'Abertura'),
    ('Encerramento', 'Encerramento'),
)


class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000, default='Aberturas e Encerramentos de ')
    categoria = models.ManyToManyField('Categoria')
    thumb = models.ImageField(upload_to='thumb_animes')
    background = models.ImageField(upload_to='background_animes')
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    temporadas = models.ManyToManyField('Temporada')

    def __str__(self):
        return self.titulo


class Episodeo(models.Model):
    anime = models.ForeignKey("Anime", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_EPISODIO)
    temporada = models.ForeignKey("Temporada", related_name="episodios", on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.anime.titulo + " " + "|" + " " + self.titulo


class Usuario(AbstractUser):
    animes_vistos = models.ManyToManyField("Anime")


class Categoria(models.Model):
    categorias = models.CharField(max_length=20)

    def __str__(self):
        return self.categorias


class Temporada(models.Model):
    temporadas = models.CharField(max_length=5)

    def __str__(self):
        return self.temporadas