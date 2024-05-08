from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from .models import Anime, Usuario
from .forms import CriarContaForm
from django.db.models import Q

class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('anime:home_animes')
        else:
            return super().get(request, *args, **kwargs)

class Home_animes(LoginRequiredMixin, ListView):
    template_name = 'home_anime.html'
    model = Anime


class Detalhes_Anime(LoginRequiredMixin, DetailView):
    template_name = 'detalhes_anime.html'
    model = Anime


    def get(self, request, *args, **kwargs):
        anime = self.get_object()
        anime.visualizacoes += 1
        anime.save()
        usuario = request.user
        usuario.animes_vistos.add(anime)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhes_Anime, self).get_context_data(**kwargs)
        filtro = Q()
        for categoria in self.get_object().categoria.all():
            filtro = filtro | Q(categoria=categoria)
        animes_relacionados = Anime.objects.filter(filtro).exclude(id=self.get_object().id)
        animes_relacionados = list(animes_relacionados)

        animes_relacionados_sem_duplicatas = {}
        for anime in animes_relacionados:
            animes_relacionados_sem_duplicatas[anime.titulo] = anime

        animes_sem_duplicatas = list(animes_relacionados_sem_duplicatas.values())
        animes_relacionados = animes_sem_duplicatas

        context["Animes_Relacionados"] = animes_relacionados
        return context


class PesquisaAnime(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Anime

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        termo_pesquisa = self.request.GET.get('query')
    
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            context['termo_pesquisa'] = termo_pesquisa
        else:
            object_list = self.model.objects.all()
            context['termo_pesquisa'] = None
        
        if object_list.exists():
            context['object_list'] = object_list
        else:
            context['nenhum_resultado'] = True
            context['object_list'] = self.model.objects.all()

        return context


class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editar_perfil.html'
    model = Usuario
    fields = ['username', 'email']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.id != self.kwargs['pk']:
                return self.redirect_to_own_profile()
        else:
            return HttpResponseRedirect(reverse('anime:login'))
        return super().dispatch(request, *args, **kwargs)

    def redirect_to_own_profile(self):
        own_profile_url = reverse('anime:editar_perfil', kwargs={'pk': self.request.user.id})
        return HttpResponseRedirect(own_profile_url)

    def get_success_url(self):
        return reverse('anime:home_animes')


class CriarConta(FormView):
    template_name = 'criar_conta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('anime:login')