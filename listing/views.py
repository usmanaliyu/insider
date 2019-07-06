from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from . models import Listing, Listing_category
from Article . models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag

from django.conf import settings
import redis



# Create your views here.

def Listing_list(request):
    instance = Listing.objects.all()
    categories = Category.objects.all()
    listing_categories = Listing_category.objects.all()

    content ={
        'instance':instance,
        'listing_categories':listing_categories,
        'categories':categories,
    }
    return render(request,'listing/listing_list.html',content)

