from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from taggit.managers import TaggableManager
from comments . models import Comment

from django_countries.fields import CountryField

# Create your models here.
class Listing_category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering =['name']
        verbose_name = 'listing_category'

    def get_absolute_url(self):
        return reverse('category_listing', args=[self.slug])

    def __str__(self):
        return self.name

class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='listing-logo/', blank=True)
    company_name = models.CharField(max_length=250, blank=False, unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    segment = models.ForeignKey(Listing_category, on_delete=models.CASCADE, default=1, )
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)

    street = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100,blank=False)
    country = CountryField(blank_label='(select country)')


    description = models.TextField(max_length=1000, blank=False)
    images = models.ImageField(upload_to='listing-images', blank=False)







    def __str__(self):
        return self.company_name
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


