from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from . models import Listing, Listing_category
from Article.models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag
from . choices import country_choice

from django.conf import settings
import redis

r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db = settings.REDIS_DB)




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
    return render(request,'listing/business_listing.html',content)




def listing_detail(request,listing_slug):
    instance = get_object_or_404(Listing, slug=listing_slug)
    categories = Category.objects.all()


    total_views = r.incr('instance:{}:views'.format(instance.id))
    r.zincrby('instance_ranking', instance.id, 1)

    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        user_data = form.cleaned_data.get('user')
        email_data = form.cleaned_data.get('email')

        parent_obj = None
        try:
            parent_id = request.POST.get('parent_id')
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=user_data,
            email=email_data,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,

        )

    comments = instance.comments
    context = {

        'instance': instance,
        'comments': comments,
        'comment_form': form,
        'total_views': total_views,
        'categories':categories,

    }
    return render(request, 'listing/business_detail.html', context)


def list_home(request):
    instance = Listing.objects.all()


    content ={
        'instance':instance,
        'country_choice':country_choice,

    }
    return render(request,'listing/listing_home.html',content)



def listing_search(request):
    qs = Listing.objects.order_by('company_name')

    if 'Keywords' in request.GET:
        keywords = request.GET['Keywords']
        if keywords:
            qs = qs.filter(description__icontains=keywords)

    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            qs = qs.filter(country__iexact=country)

    content ={
        'instance':qs,
        'country_choice':country_choice,

    }
    return render(request,'listing/listing_search.html',content)



