from django import forms
from django.forms import ValidationError

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Error1',
                            params={'valor':value})


class ContactoForm(forms.Form):

    nombre = forms.CharField(
            label='Nombre',
            required=True,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            error_messages={
                    'required': 'Por favor completa el campo',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Ingrese su email'})
            )
    telefono = forms.CharField(
            label='Telefono',
            max_length=12,
            widget= forms.TextInput(attrs={'class':'form-control','type':'tel','placeholder':'Enter your phone number...'})
            )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':7,'type':'textarea','placeholder':'Enter your messages...'})
            )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("El mensaje no puede ser menor a 10 caracteres")
        return data
    
