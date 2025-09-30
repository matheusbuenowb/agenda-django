from django.urls import path
from contact import views 

app_name = 'contact' # Namespace for the app

#aqui são criadas as rotas da aplicação contact e index

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.contact, name='contact'), #parâmetro dinâmico [int:contact_id]
]
