from django import forms
from .models import Automation

class AutomationForm(forms.ModelForm):
    class Meta:
        model = Automation
        fields = ['name', 'trigger_type', 'trigger_value', 'action', 'target_campaign']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'trigger_type': forms.Select(attrs={'class': 'form-select'}),
            'trigger_value': forms.TextInput(attrs={'class': 'form-control'}),
            'action': forms.Select(attrs={'class': 'form-select'}),
            'target_campaign': forms.Select(attrs={'class': 'form-select'}),
        }
