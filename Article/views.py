from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.contenttypes.models import ContentType
from . models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.cache import cache_page
from contact .forms import SubscribeForm
from contact .models import Subscribe


from django.conf import settings




# Create your views here.

@cache_page(60 * 15)
def home(request):
    instance_list = Article.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(instance_list, 5)
    page = request.GET.get('page')
    instance = paginator.get_page(page)

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

    content = {
        'instance': instance,
        'categories': categories,
        'sub':sub,

    }
    return render(request, 'blog/home.html', content)


@cache_page(60 * 15)
def Articles_list(request):
    instance_list= Article.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(instance_list, 10)
    page = request.GET.get('page')
    instance = paginator.get_page(page)

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

    content ={
        'instance':instance,
        'categories':categories,
        'sub':sub,
    }
    return render(request,'blog/article_list.html',content)


@cache_page(60 * 15)
def list_of_articles_by_category(request, category_slug):

    instance = Article.objects.all()
    categories = Category.objects.all()

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        instance_list = instance.filter(category=category)
        paginator = Paginator(instance_list, 10)
        page = request.GET.get('page')
        instance = paginator.get_page(page)


    context = {
        'categories':categories,
        'instance':instance,
        'category':category,
        'sub':sub,
               }
    return render(request, 'blog/category_list.html',context)




@cache_page(60 * 15)
def tagged(request, tags_slug):
    categories = Category.objects.all()
    tag_category = Tag.objects.all()
    instance = Article.objects.all()

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')


    if tags_slug:
        tags = get_object_or_404(Tag, slug=tags_slug)
        instance_list = instance.filter(tags=tags)
        paginator = Paginator(instance_list, 10)
        page = request.GET.get('page')
        instance = paginator.get_page(page)


    context = {
        'categories':categories,
        'instance':instance,
        'tag':tags,
        'tag_category':tag_category,
        'sub':sub,

               }
    return render(request, 'blog/tag_list_view.html',context)






@cache_page(60 * 15)
def events(request):

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

    content={
        'sub':sub,
    }
    return render(request,'blog/events.html',content)









@cache_page(60 * 15)
def detail(request,article_slug):
    instance = get_object_or_404(Article,slug=article_slug)
    categories = Category.objects.all()



    similar_posts = instance.tags.similar_objects()[:5]







    initial_data={
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }
    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

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
        messages.success(request,'Comment added successfully!!')


    comments = instance.comments
    context={
        'title': instance.title,
        'instance':instance,
        'comments': comments,
        'comment_form':form,

        'similar_posts':similar_posts,
        'categories':categories,
        'sub':sub,



    }
    return render(request,'blog/detail_view.html',context)




@cache_page(60 * 15)
def search(request):
    categories = Category.objects.all()
    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')
    if request.GET:
        search_term = request.GET['search_term']
        search_result = Article.objects.filter(
            Q(title__icontains=search_term)




        )
        content ={
            'search_term':search_term,
            'instance':search_result,
            'categories':categories,
            'sub':sub,
        }
        return render(request,'blog/search.html',content)
    else:
        return redirect('home')