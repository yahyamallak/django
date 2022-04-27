from django.shortcuts import render
from .models import *
from .forms import BookForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()


    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
    }
    return render(request, 'pages/index.html', context)


def books(request):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)