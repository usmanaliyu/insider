from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . forms import UserRegistrationForm, UserUpdateForm
from listing .models import Listing
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView


# Create your views here.



class SignUp(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = '../signup_done'

def signup_done(request):
    return render(request,'registration/signup_done.html')




def profile(request):
    user = request.user

    instance=Listing.objects.filter(user=request.user).order_by('company_name')
    template = 'user/profile.html'
    return render(request,template,{'instance':instance,'user':user})





@login_required()
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account is updated!')
            return redirect('home')
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

