from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            'first_name',
            'last_name',
            'phone',]
        
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None, 
            ValidationError(
                'Erro de validação no campo first_name',
                code = "invalid"
            )
        )