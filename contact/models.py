from django.db import models
from django.utils import timezone

# Create your models here.

# id (criado automaticamente pelo Django como chave primária)

class Contact(models.Model): # herdando de models.Model
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) #blank=True permite que o campo seja opcional
    email = models.EmailField(max_length=254, blank=True) #blank=True permite que o campo seja opcional
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now) # data e hora de criação do contato
    description = models.TextField(blank=True) # campo de texto maior, opcional 

    def __str__(self):
        return f"Contact from {self.name} <{self.email}>"