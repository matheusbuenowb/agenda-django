from django.urls import path
from contact import views 

app_name = 'contact' # Namespace for the app

#aqui são criadas as rotas da aplicação contact e index

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), 

    #contact (CRUD)
    path('contact/create/', views.contact, name='contact'), #parâmetro dinâmico [int:contact_id]
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), #READ
    path('contact/<int:contact_id>/update/', views.contact, name='contact'), #UPDATE
    path('contact/<int:contact_id>/delete/', views.contact, name='contact'), #DELETE

]
