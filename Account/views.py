from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . forms import UserRegistrationForm, UserUpdateForm

# Create your views here.



class SignUp(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = '../signup_done'

def signup_done(request):
    return render(request,'registration/signup_done.html')

def profile(request):
    return render(request,'user/profile.html')


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

