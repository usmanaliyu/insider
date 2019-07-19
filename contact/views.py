from django.shortcuts import render
from django.contrib import messages
from . forms import ContactForm,SubscribeForm



# Create your views here.


def contact_page(request):

    contact_form = ContactForm(request.POST)
    sub = SubscribeForm(request.POST)
    if sub.is_valid():
        email_data = sub.cleaned_data.get('email')
        new_comment, created = Subscribe.objects.get_or_create(
            email=email_data,
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
