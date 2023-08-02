from django.shortcuts import render
from django.views.generic import  ListView
from .models import Author

class AuthorList(ListView):
    model = Author
    ordering = 'rating_Author'
    template_name = 'authors.html'
    context_object_name = 'author'



