from django.shortcuts import redirect, render
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone',]

def create(request):

    if request.method == 'POST':
        context = { 
            'form': ContactForm(request.POST)
        }

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



    