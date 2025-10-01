from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404

def index(request):

    contacts = Contact.objects.filter(show = True).order_by('-id')[10:20] #ordena do mais novo para o mais antigo
    #orderna por id em ordem decrescente, por isso -id
    #filtro para mostrar apenas os contatos com show = True
    #o [0:10] limita a quantidade de contatos mostrados para 10, é um fatiamento de lista do Python
    #[10:20] pula os 10 primeiros e mostra do 11 ao 20, é um OFFSET
    
    print(contacts.query) #mostra a query SQL gerada pelo Django no terminal, genial para debug


    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(

        request, 
        'contact/index.html',
        context 
    )


def contact(request, contact_id):

    #duas formas de pegar um contato específico

    #single_contact = Contact.objects.filter(pk = contact_id).first()

    '''if single_contact is None:
        raise Http404()
'''
    single_contact = get_object_or_404(
        Contact, pk = contact_id, show = True#aqui simplifica o código acima
    )

    #single foi só para nao conflitar com o def contact


    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
        
    }

    return render(

        request, 
        'contact/contact.html',
        context 
    )