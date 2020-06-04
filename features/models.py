from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.TextField()
    slug = models.SlugField(max_length=150)
    created_date = models.DateTimeField(editable=False, default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='author_feature', on_delete=models.CASCADE, null=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name="feature_upvotes")

    STATUS_CHOICES = ( ('to do', 'to do'), ('Doing', 'Doing'), ('Done', 'Done') )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='to do')
    
    def __str__(self):
        return self.title

    # Ordered by the most recent modified date
    class Meta:
        ordering = ('-modified_date',)

    def total_upvotes(self):
        return self.upvotes.count()

    def get_absolute_url(self):
        return reverse("feature_detail", args=[str(self.id), str(self.slug)])

    def save(self, *args, **kwargs):
        """ This will automatically creates a slug when we create or edit a bug
            Find on https://books.agiliq.com/projects/django-orm-cookbook/en/latest/slugfield.html
        """
        self.slug = slugify(self.title)

        """ On save, update timestamps. Update the modified date when a post has been updated.
        """
        self.modified_date = timezone.now()
        super(Feature, self).save(*args, **kwargs)