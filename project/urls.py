from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')), # a raiz do site vai para o contact
]
