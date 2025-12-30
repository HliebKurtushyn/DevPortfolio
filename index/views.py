from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html', {"article": {"date": "12.11.2024", "title": "Text here", "author": "<NAME>"}})


def about_view(request):
    return render(request, 'index/about/about.html')


def contacts_view(request):
    return render(request, 'index/about/contacts.html')
