# app/forms.py

from django import forms
from app.models import Entreprise


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = [
            'civilite', 'directeur', 'name', 'domaine', 'email', 'contact', 'link', 'location'
        ]
