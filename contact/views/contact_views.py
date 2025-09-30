from django.shortcuts import render
from contact.models import Contact

def index(request):

    contacts = Contact.objects.filter(show = True).order_by('-id')[10:20] #ordena do mais novo para o mais antigo
    #orderna por id em ordem decrescente, por isso -id
    #filtro para mostrar apenas os contatos com show = True
    #o [0:10] limita a quantidade de contatos mostrados para 10, é um fatiamento de lista do Python
    #[10:20] pula os 10 primeiros e mostra do 11 ao 20, é um OFFSET
    
    print(contacts.query) #mostra a query SQL gerada pelo Django no terminal, genial para debug


    context = {
        'contacts': contacts,
    }

    return render(

        request, 
        'contact/index.html',
        context 
    )