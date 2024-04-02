from .models import Anime

def lista_animes_recentes(request):
    animes_recentes = Anime.objects.order_by('-data_criacao')[0:12]
    return {"lista_animes_recentes": animes_recentes}

def lista_animes_popular(request):
    animes_populares = Anime.objects.all().order_by('-visualizacoes')[0:12]
    if animes_populares:
        anime_destaque = animes_populares[0]
    else:
        anime_destaque = None
    return {"lista_animes_popular": animes_populares, 'anime_destaque': anime_destaque}