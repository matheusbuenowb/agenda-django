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
            'email',
            'description',
            'category',
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

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name:       
            msg = ValidationError(
                    'O primeiro nome não pode ser igual ao último nome',
                    code = "invalid"
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()  

    def clean_first_name(self):

        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'first_name', 
                ValidationError(
                    'O primeiro nome não pode ser igual ao último nome',
                    code = "invalid"
                )
            )
        
        return first_name