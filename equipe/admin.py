from django.contrib import admin
from .models import Pesquisador
# Register your models here.

#admin.site.register(Pesquisador)

class PesquisadorAdmin(admin.ModelAdmin):
    search_fields = ['nome',]

admin.site.register(Pesquisador, PesquisadorAdmin)