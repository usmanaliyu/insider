from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from taggit.managers import TaggableManager
from comments . models import Comment

from django_countries.fields import CountryField
from django_countries import Countries

# Create your models here.


class AfricanCountries(Countries):
    only = [
        'DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV',
        'CF', 'KM', 'CD', 'DJ', 'EG', 'GQ', 'ER',
        'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI',
        'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML',
        'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG',
        'CG', 'RE', 'RW', 'SH', 'ST', 'SN', 'SC',
        'SL',

    ]



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
    country = models.CharField(max_length=200, choices=(
                            ('DZ', 'Algeria'),
                            ('AO', 'Angola'),
                            ('BJ', 'Benin'),
                            ('BW', 'Botswana'),
                            ('BF', 'Burkina Faso'),
                            ('BI', 'Burundi'),
                            ('CM', 'Cameroon'),
                            ('CV', 'Cape Verde'),
                            ('CF', 'Central African Republic'),
                            ('KM', 'Comoros'),
                            ('CD', 'Democratic Republic of Congo'),
                            ('DJ', 'Djibouti'),
                            ('EG', 'Egypt'),
                            ('GQ', 'Equatorial Guinea'),
                            ('ER', 'Eritrea'),
                            ('ET', 'Ethiopia'),
                            ('GA', 'Gabon'),
                            ('GM', 'Gambia'),
                            ('GH', 'Ghana'),
                            ('GN', 'Guinea'),
                            ('GW', 'Guinea-Bissau'),
                            ('CI', 'Ivory Coast'),
                            ('KE', 'Kenya'),
                            ('LS', 'Lesotho'),
                               ('LR', 'Liberia'),
                               ('LY', 'Libya'),
                               ('MG', 'Madagascar'),
                               ('MW', 'Malawi'),
                               ('ML', 'Mali'),
                               ('MR', 'Mauritania'),
                               ('MU', 'Mauritius'),
                               ('MA', 'Morocco'),
                               ('MZ', 'Mozambique'),
                               ('NA', 'Namibia'),
                               ('NE', 'Niger'),
                               ('NG', 'Nigeria'),
                               ('CG', 'Republic of the Congo'),
                               ('RE', 'Reunion'),
                               ('RW', 'Rwanda'),
                               ('SH', 'Saint Helena'),
                               ('ST', 'Sao Tome and Principe'),
                               ('SN', 'Senegal'),
                               ('SC', 'Seychelles'),
                               ('SL', 'Sierra Leone'),
    ))


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


