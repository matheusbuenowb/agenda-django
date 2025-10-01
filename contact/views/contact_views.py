from django.shortcuts import redirect, render
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q

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


def search(request):

    search_value = request.GET.get('q', '').strip() #pega o valor do input name = q do form e o strip tira espaços em branco
    print(search_value)

    if search_value == '':
        return redirect('contact:index') #se o campo de busca estiver vazio, redireciona para a index

    contacts = Contact.objects.filter(show = True).filter(
        Q(first_name__icontains= search_value) |
        Q(last_name__icontains= search_value) |
        Q(phone__icontains= search_value) |
        Q(email__icontains= search_value)
        ).order_by('-id')
    # com isso se eu digitar "jo" ele traz "João" e "joana", o icontains é case insensitive
    #O Q envolvido serve como se fosse um OR (OU) entre os dois filtros
    #é uma pesquisa basica do google, traz qualquer coisa que contenha o valor buscado
    #mas é simples, se colocar nome + sobrenome nao traz nada, nem se colocar parte do nome e parte do sobrenome
    #pois a lógica é OU, não E, teria que fazer separado e ficaria demasiado complexo
    #ex: eu teria que separar o search_value em partes e fazer um Q para cada parte
    
    print(contacts.query) #mostra a query SQL gerada pelo Django no terminal, genial para debug


    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
        'search_value': search_value #remove os espaços em branco com o strip acima
    }

    return render(

        request, 
        'contact/index.html',
        context 
    )