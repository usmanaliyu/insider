from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from taggit.managers import TaggableManager
from comments . models import Comment
from django.utils.text import slugify


# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering =['name']
        verbose_name = 'category'

    def get_absolute_url(self):
        return reverse('business_category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='listing-logo/', blank=False)
    company_name = models.CharField(max_length=250, blank=False, unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1,)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)

    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100,blank=False)
    country = models.CharField(max_length=200, choices=(
                            ('Algeria', 'Algeria'),
                            ('Angola', 'Angola'),
                            ('Benin', 'Benin'),
                            ('Botswana', 'Botswana'),
                            ('Burkina Faso', 'Burkina Faso'),
                            ('Burundi', 'Burundi'),
                            ('Cameroon', 'Cameroon'),
                            ('Cape Verde', 'Cape Verde'),
                            ('Central African Republic', 'Central African Republic'),
                            ('Comoros', 'Comoros'),
                            ('Democratic Republic of Congo', 'Democratic Republic of Congo'),
                            ('Djibouti', 'Djibouti'),
                            ('Egypt', 'Egypt'),
                            ('Equatorial Guinea', 'Equatorial Guinea'),
                            ('Eritrea', 'Eritrea'),
                            ('Ethiopia', 'Ethiopia'),
                            ('Gabon', 'Gabon'),
                            ('Gambia', 'Gambia'),
                            ('Ghana', 'Ghana'),
                            ('Guinea', 'Guinea'),
                            ('Guinea-Bissau', 'Guinea-Bissau'),
                            ('Ivory Coast', 'Ivory Coast'),
                            ('Kenya', 'Kenya'),
                            ('Lesotho', 'Lesotho'),
                               ('Liberia', 'Liberia'),
                               ('Libya', 'Libya'),
                               ('Madagascar', 'Madagascar'),
                               ('Malawi', 'Malawi'),
                               ('Mali', 'Mali'),
                               ('Mauritania', 'Mauritania'),
                               ('Mauritius', 'Mauritius'),
                               ('Morocco', 'Morocco'),
                               ('Mozambique', 'Mozambique'),
                               ('Namibia', 'Namibia'),
                               ('Niger', 'Niger'),
                               ('Nigeria', 'Nigeria'),
                               ('Republic of the Congo', 'Republic of the Congo'),
                               ('Reunion', 'Reunion'),
                               ('Rwanda', 'Rwanda'),
                               ('Saint Helena', 'Saint Helena'),
                               ('Sao Tome and Principe', 'Sao Tome and Principe'),
                               ('Senegal', 'Senegal'),
                               ('Seychelles', 'Seychelles'),
                               ('Sierra Leone', 'Sierra Leone'),
    ))

    motto = models.TextField(max_length=1000, blank=True)
    description = models.TextField(max_length=5000, blank=False)
    tags = TaggableManager(verbose_name='Products(separate with comma)')
    terms = models.CharField (verbose_name='I agree to Terms and Conditions',max_length=50,blank=False,default=1, choices=
                                   (
                                       ('yes','Yes'),


                                   ))

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

    def _get_unique_slug(self):
        slug = slugify(self.company_name)
        unique_slug = slug
        num =1
        while Listing.objects.filter(slug=unique_slug).exists():
            unique_slug ='{}-{}'.format(slug,num)
            num +=1
        return unique_slug
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug =self._get_unique_slug()
        super().save(*args,**kwargs)




