from django.urls import path
from contact import views 

app_name = 'contact' # Namespace for the app

urlpatterns = [
    path('', views.index, name='index'),
]
