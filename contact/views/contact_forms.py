from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
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


def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk = contact_id, show = True
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
    