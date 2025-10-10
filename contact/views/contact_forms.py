from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from contact.forms import ContactForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login') # isso redireciona para o login se nao estiver logado
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        
        context = { 
            'form': form,
            'form_action': form_action  
        }

        if form.is_valid():
            contact = form.save() #isso já salva no sgbd
            return redirect('contact:update', contact_id = contact.pk)

        return render(
            request, 
            'contact/create.html',
            context 
        )
    

    context = { 
        'form': ContactForm()
    }

    return render(

        request, 
        'contact/create.html',
        context 
    )

@login_required(login_url='contact:login') # isso redireciona para o login se nao estiver logado
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk = contact_id, show = True, owner = request.user
    )
    form_action = reverse('contact:update', args =(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance = contact)
        context = { 
            'form': form,
            'form_action': form_action  
        }

        if form.is_valid():
            contact = form.save() #isso já salva no sgbd
            return redirect('contact:update', contact_id = contact.pk)

        return render(
            request, 
            'contact/create.html',
            context 
        )
    

    context = { 
        'form': ContactForm(instance = contact),
        'form_action': form_action
    }

    return render(

        request, 
        'contact/create.html',
        context 
    )

@login_required(login_url='contact:login') # isso redireciona para o login se nao estiver logado
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk = contact_id, show = True
    )

    confirmation = request.POST.get('confirmation', 'no')
    print(confirmation)

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    
    return render (
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )