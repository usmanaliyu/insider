from django.shortcuts import render
from django.contrib import messages
from . forms import ContactForm


# Create your views here.


def contact_page(request):

    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        create_contact = contact_form.save()
        messages.success(request, 'Message sent successfully!!')

    content={
        'contact_form':contact_form,
    }
    return render(request,'contact/contact.html',content)
