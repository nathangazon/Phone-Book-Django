from contatos.models import Contato
from django import forms
from django import forms

from contatos.models import Contato


# Create your models here.

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar',)
