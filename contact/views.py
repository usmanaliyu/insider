from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from Article . models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag

from . forms import ContactForm

from django.conf import settings
import redis


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db = settings.REDIS_DB)

# Create your views here.


def contact_page(request):
    categories = Category.objects.all()
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        create_contact = contact_form.save()

    content={
        'contact_form':contact_form,
        'categories':categories,
    }
    return render(request,'contact/contact.html',content)
