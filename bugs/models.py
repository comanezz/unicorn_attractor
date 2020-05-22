from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Bug(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.TextField()
    slug = models.SlugField(max_length=120)

    STATUS_CHOICES = (
        ('to do', 'to do'),
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='to do')
    author = models.ForeignKey(User, related_name='author_bug', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    """ This will automatically creates a slug when we create or edit a bug
        Find on https://books.agiliq.com/projects/django-orm-cookbook/en/latest/slugfield.html
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Bug, self).save(*args, **kwargs)