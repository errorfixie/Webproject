from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from books.models import BookCategory, Publisher, Book

class BookList(generic.ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'total_book_list'

class BookDetailView(generic.DetailView):
    queryset = Book.objects.all()
    template_name = 'books/detail.html'
    context_object_name = 'book_detail'