from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'blog/home.html')

def articles(request):
    return render(request,'blog/articles_list.html')

def detail(request):
    return render(request,'blog/detail_view.html')

def categorylist(request):
    return render(request,'blog/category_list.html')

def events(request):
    return render(request,'blog/events.html')

def contact(request):
    return render(request,'blog/contact.html')