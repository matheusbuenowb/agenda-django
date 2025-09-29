from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')), # a raiz do site vai para o contact
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# para servir arquivos de mídia durante o desenvolvimento, para acessar as imagens enviadas via navegador
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#nao é necessario em producao, apenas em desenvolvimento, para servir arquivos 
# estaticos (css, js, imagens) durante o desenvolvimento