from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.contenttypes.models import ContentType
from . models import Article, Category
from django.db.models import Q
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag

from django.conf import settings
import redis


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db = settings.REDIS_DB)


# Create your views here.

class home(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'instance'

class Articles_list(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'instance'
    ordering = ['-pub_date']

def detail(request):
    return render(request,'blog/detail_view.html')

def list_of_articles_by_category(request, category_slug):
    categories = Category.objects.all()
    instance = Article.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        instance = instance.filter(category=category)


    context = {
        'categories':categories,
        'instance':instance,
        'category':category
               }
    return render(request, 'blog/category_list.html',context)


class ToggleMixen(object):
    def get_context_data(self,**kwargs):
        context = super(ToggleMixen,self).get_context_data(**kwargs)
        context['tags']= Tag.objects.all()
        return context

class tag_list_view(ToggleMixen,ListView):
    model = Article
    template_name = 'blog/tag_list_view.html'
    context_object_name = 'instance'

    def get_queryset(self):
        return Article.objects.filter(tags__slug=self.kwargs.get('slug'))



def tagged(request, tags_slug):
    categories = Tag.objects.all()
    instance = Article.objects.all()


    if tags_slug:
        tags = get_object_or_404(Tag, slug=tags_slug)
        instance = instance.filter(tags=tags)


    context = {
        'categories':categories,
        'instance':instance,
        'tag':tags

               }
    return render(request, 'blog/tag_list_view.html',context)





def categorylist(request):
    return render(request,'blog/category_list.html')

def events(request):
    return render(request,'blog/events.html')

def contact(request):
    return render(request,'blog/contact.html')








def detail(request,id):
    instance = get_object_or_404(Article,pk=id)
    total_views = r.incr('instance:{}:views'.format(instance.id))
    r.zincrby('instance_ranking', instance.id, 1)


    initial_data={
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

        parent_obj=None
        try:
            parent_id = request.POST.get('parent_id')
        except:
            parent_id = None


        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user = user_data,
            email=email_data,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,


        )


    comments = instance.comments
    context={
        'title': instance.title,
        'instance':instance,
        'comments': comments,
        'comment_form':form,
        'total_views':total_views,


    }
    return render(request,'blog/detail_view.html',context)


def instance_ranking(request):
    instance_ranking = r.zrange('instance_ranking', 0, -1, desc=True)[:10]
    instance_ranking_ids = [int(id) for id in instance_ranking]
    most_viewed = list(Article.objects.filter(id__in=instance_ranking_ids))
    most_viewed.sort(key=lambda x: instance_ranking_ids.index(x.id))

    return render(request, 'blog/ranking.html',
                  {'section':'instances',
                   'most_viewed': most_viewed})