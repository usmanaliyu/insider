from django.shortcuts import render
from django.contrib import messages
from . forms import ContactForm,SubscribeForm
from .models import Subscribe
from django.views.decorators.cache import cache_page



# Create your views here.

@cache_page(60 * 15)
def contact_page(request):

    contact_form = ContactForm(request.POST)
    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('s_email')
        new_comment, created = Subscribe.objects.get_or_create(
            S_email=email_data,
        )
        messages.success(request, 'You have subscribed successfully!!')
    if contact_form.is_valid():
        create_contact = contact_form.save()
        messages.success(request, 'Message sent successfully!!')

    content={
        'contact_form':contact_form,
        'sub':sub,
    }
    return render(request,'contact/contact.html',content)
