from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from . models import Listing, Category
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag
from . choices import country_choice
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from contact .forms import SubscribeForm
from contact .models import Subscribe
from django.views.decorators.cache import cache_page


from django.conf import settings







# Create your views here.
@cache_page(60 * 15)
def Listing_list(request):
    instance_list = Listing.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(instance_list, 12)
    page = request.GET.get('page')
    instance = paginator.get_page(page)
    listing_categories = Category.objects.all()

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

    content ={
        'instance':instance,
        'listing_categories':listing_categories,
        'categories':categories,
        'country_choice': country_choice,
        'sub':sub,
    }
    return render(request,'listing/business_listing.html',content)



@cache_page(60 * 15)
def listing_detail(request,listing_slug):
    instance = get_object_or_404(Listing, slug=listing_slug)
    categories = Category.objects.all()
    listing_categories = Category.objects.all()




    initial_data = {
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
        messages.success(request, 'Review added successfully!!')

    comments = instance.comments
    context = {

        'instance': instance,
        'comments': comments,
        'comment_form': form,

        'categories':categories,
        'sub':sub,
        'listing_categories': listing_categories,

    }
    return render(request, 'listing/business_detail.html', context)

@cache_page(60 * 15)
def list_home(request):
    instance = Listing.objects.all()
    categories = Category.objects.all()

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

    content ={
        'instance':instance,
        'country_choice':country_choice,
        'categories':categories,
        'sub':sub,

    }
    return render(request,'listing/listing_home.html',content)


@cache_page(60 * 15)
def listing_search(request):
    qs = Listing.objects.order_by('company_name')
    categories = Category.objects.all()
    listing_categories = Category.objects.all()

    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('S_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')

    Keywords = request.GET['Keywords']

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
        'Keywords': Keywords,
        'categories':categories,
        'listing_categories':listing_categories,
        'sub':sub,


    }
    return render(request,'listing/listing_search.html',content)



class listcreate(LoginRequiredMixin,CreateView):
    model = Listing
    fields = ['logo','company_name','category','description','motto','tags','phone_number','email','street','city','country','terms']
    template_name = 'listing/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user


        return super().form_valid(form)


    success_url = 'account/profile'



class listupdate(LoginRequiredMixin,UpdateView):
    model = Listing
    fields = ['logo','company_name','category','description','motto','tags','phone_number','email','street','city','country']
    template_name = 'listing/update.html'


    def form_valid(self, form):
        if form.instance.user == self.request.user:

            return super().form_valid(form)
        else:
            raise PermissionDenied


    success_url = '../account/profile'


class listdelete(LoginRequiredMixin,DeleteView):
    model = Listing
    fields = ['logo','company_name','category','description','motto','tags','phone_number','email','street','city','country']
    template_name = 'listing/delete.html'


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            messages.success(request, 'Listing deleted successfully!!')
            return HttpResponseRedirect(self.get_success_url())

        else:
            raise PermissionDenied



    success_url = '../account/profile'


@cache_page(60 * 15)
def listtag(request, tags_slug):
    categories = Category.objects.all()
    tag_category = Tag.objects.all()
    instance = Listing.objects.all()

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

        paginator = Paginator(instance_list, 12)
        page = request.GET.get('page')
        instance = paginator.get_page(page)





    context = {
        'categories':categories,
        'instance':instance,
        'tag':tags,
        'tag_category':tag_category,
        'sub':sub,


               }
    return render(request, 'listing/list_tag.html',context)

@cache_page(60 * 15)
def list_of_business_by_category(request, category_slug):

    instance = Listing.objects.all()
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

        paginator = Paginator(instance_list, 12)
        page = request.GET.get('page')
        instance = paginator.get_page(page)



    context = {
        'categories':categories,
        'instance':instance,
        'category':category,
        'sub':sub,
        'country_choice': country_choice,
               }
    return render(request, 'listing/category_list.html',context)
