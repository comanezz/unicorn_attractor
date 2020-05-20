from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.TextField()

    STATUS_CHOICES = (
        ('to do', 'to do'),
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='to do')

    def __str__(self):
        return self.title