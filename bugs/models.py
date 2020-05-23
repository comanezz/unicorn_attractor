from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Bug(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.TextField()
    slug = models.SlugField(max_length=120)
    created_date = models.DateTimeField(editable=False, default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = (
        ('to do', 'to do'),
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='to do')
    author = models.ForeignKey(User, related_name='author_bug', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ This will automatically creates a slug when we create or edit a bug
            Find on https://books.agiliq.com/projects/django-orm-cookbook/en/latest/slugfield.html
        """
        self.slug = slugify(self.title)

        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        super(Bug, self).save(*args, **kwargs)