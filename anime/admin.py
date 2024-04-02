from django.contrib import admin
from .models import Anime, Episodeo, Usuario, Categoria, Temporada
from django.contrib.auth.admin import UserAdmin


campos = list(UserAdmin.fieldsets)
campos.append(("Histórico", {'fields': ('animes_vistos',)}))
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Anime)
admin.site.register(Episodeo)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Categoria)
admin.site.register(Temporada)