from django.db import models

# Create your models here.
class Bug(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title