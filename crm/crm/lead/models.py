from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    source = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Lost', 'Lost'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


