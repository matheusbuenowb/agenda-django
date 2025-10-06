from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):

    first_name = forms.CharField( #sobrescrevendo o campo first_name do modelo Contact  
        widget = forms.TextInput(
            attrs = {
                'class': 'classe-a classe-b',
                'placeholder': 'Digite o primeiro nome',
            }   
        ),
        label = 'Primeiro Nome',
        help_text = 'Digite o primeiro nome do contato',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({ #attrs é um dicionário
            'class': 'classe-a classe-b',
            'placeholder': 'Digite o primeiro nome',
        })
    
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'classe-a classe-b',
                    'placeholder': 'Digite o primeiro nome',
                }
            )
        }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None, 
            ValidationError(
                'Erro de validação no campo first_name',
                code = "invalid"
            )
        )