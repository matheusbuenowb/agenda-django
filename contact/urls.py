from django.urls import path
from contact import views 

app_name = 'contact' # Namespace for the app

#aqui são criadas as rotas da aplicação contact e index

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), 

    #contact (CRUD)
    path('contact/create/', views.create, name='create'), #parâmetro dinâmico [int:contact_id]
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), #READ
    path('contact/<int:contact_id>/update/', views.update, name='update'), #UPDATE
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), #DELETE

]
