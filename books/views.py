from django.shortcuts import render
from .models import Books
from django.views.generic import ListView


# Create your views here.
class BookListView(ListView):
    model = Books

    template_name = 'books_list.html'