from django.contrib import admin
from django.urls import path, include, reverse_lazy
from .views import Homepage, Home_animes, Detalhes_Anime, PesquisaAnime, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_view

app_name = 'anime'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('animes/', Home_animes.as_view(), name='home_animes'),
    path('animes/<int:pk>', Detalhes_Anime.as_view(), name='detalhes_anime'),
    path('search/', PesquisaAnime.as_view(), name='pesquisa_anime'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/edit/<int:pk>', EditarPerfil.as_view(), name='editar_perfil'),
    path('criarconta/', CriarConta.as_view(), name='criar_conta'),
    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='mudar_senha.html', success_url=reverse_lazy('anime:home_animes')), name='mudar_senha')
]
