from django import forms
from .models import Campaign
from lead.models import Lead

class CampaignForm(forms.ModelForm):
    leads = forms.ModelMultipleChoiceField(
        queryset=Lead.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control select2',  # Select2 uses this class
            'multiple': 'multiple',
        }),
        required=False
    )

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'end_date', 'leads']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
