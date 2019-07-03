from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.contenttypes.models import ContentType
from . models import Article, Category
from django.db.models import Q
from comments.forms import CommentForm
from comments.models import Comment

# Create your views here.

class home(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'instance'

def articles(request):
    return render(request,'blog/articles_list.html')

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




def categorylist(request):
    return render(request,'blog/category_list.html')

def events(request):
    return render(request,'blog/events.html')

def contact(request):
    return render(request,'blog/contact.html')








def detail(request,id):
    instance = get_object_or_404(Article,pk=id)

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
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj

        )


    comments = instance.comments
    context={
        'title': instance.title,
        'instance':instance,
        'comments': comments,
        'comment_form':form,


    }
    return render(request,'blog/detail_view.html',context)

