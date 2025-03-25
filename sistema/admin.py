from django.contrib import admin

from sistema import models

# Aqui fica o registro do Usuário
@admin.register(models.Usuário)
class UsuárioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','ativo',)   