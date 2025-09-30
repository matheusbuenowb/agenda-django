from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# id (criado automaticamente pelo Django como chave primária)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model): # herdando de models.Model
    first_name = models.CharField(max_length=50) #blank=True permite que o campo seja opcional
    last_name = models.CharField(max_length=50, blank=True) #blank=True permite que o campo seja opcional
    email = models.EmailField(max_length=254, blank=True) #blank=True permite que o campo seja opcional
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now) # data e hora de criação do contato
    description = models.TextField(blank=True) # campo de texto maior, opcional 
    show = models.BooleanField(default=True) # campo booleano para mostrar ou não o contato
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True) # campo para upload de imagem, opcional
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, blank=True
    )  # chave estrangeira para a categoria, opcional
    #on delete serve para definir o que acontece quando a categoria é deletada
    # SET_NULL: define o campo como NULL, ou seja, quando apagar a categoria, o campo category do contato vira NULL
    # CASCADE: deleta o contato junto com a categoria, deleta TUDO, CUIDADO
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}" # o que eu vou ver 
    #quando chamar o objeto Contact no shell do Django