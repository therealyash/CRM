from django.db import models
from campaign.models import Campaign

class Automation(models.Model):
    TRIGGER_CHOICES = [
        ('Time-based', 'Time-based'),
        ('Lead Status', 'Lead Status'),
    ]

    ACTION_CHOICES = [
        ('Send Email', 'Send Email'),
        ('Add to Campaign', 'Add to Campaign'),
    ]

    name = models.CharField(max_length=100)
    trigger_type = models.CharField(max_length=50, choices=TRIGGER_CHOICES)
    trigger_value = models.CharField(max_length=100, help_text="e.g. 'Qualified' or '2025-07-20'")
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    target_campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
