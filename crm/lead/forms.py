from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'source', 'status']
        widgets = {
            'status':forms.Select(attrs={'class': 'form-select'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'})
        }

