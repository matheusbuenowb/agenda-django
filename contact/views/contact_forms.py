from django.shortcuts import redirect, render
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from contact.forms import ContactForm

def create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = { 
            'form': form
        }

        if form.is_valid():
            form.save() #isso já salva no sgbd
            return redirect('contact:create')

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



    