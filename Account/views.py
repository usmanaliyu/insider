from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . forms import UserRegistrationForm, UserUpdateForm
from listing .models import Listing, Category
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from django.contrib import messages




# Create your views here.



class SignUp(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = '../signup_done'

def signup_done(request):
    return render(request,'registration/signup_done.html')


@login_required()
def profile(request):
    user = request.user

    instance_list=Listing.objects.filter(user=request.user).order_by('company_name')

    paginator = Paginator(instance_list, 10)
    page = request.GET.get('page')
    instance = paginator.get_page(page)
    listing_categories = Category.objects.all()

    content={
        'instance':instance,
        'user':user,
        'listing_categories':listing_categories,

    }

    return render(request,'user/profile.html',content)








@login_required()
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account is updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context = {
        'u_form':u_form,

        }
        return render(request,'user/profile_update.html', context)




class UserList(ListView):
    model = Listing
    context_object_name = 'instance'
    template_name = 'user/user_list.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Listing.objects.filter(user=user)

def term_of_use(request):
    return render(request,'user/termofuse.html')