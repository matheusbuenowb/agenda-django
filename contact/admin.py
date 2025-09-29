from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
   list_display = 'first_name', 'last_name', 'email', 'phone', 'created_at' #mostra essas colunas na lista de contatos
   ordering = 'id', #ordena por id
   search_fields = 'id', 'first_name', 'last_name', 'email', 'phone' #busca por esses campos
   list_max_show_all = 50 #limita a quantidade de contatos mostrados na lista
   list_editable = 'email','phone' #permite editar esses campos diretamente na lista de contatos

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = 'name', #mostra essas colunas na lista de categorias
   ordering = '-id', #ordena por id
