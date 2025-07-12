from django.db import models
from lead.models import Lead

# Create your models here.

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    leads = models.ManyToManyField(Lead, blank=True)

    def __str__(self):
        return self.name



