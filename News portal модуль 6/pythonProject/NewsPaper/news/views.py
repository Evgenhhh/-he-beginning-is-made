from django.shortcuts import render

from django.views.generic import ListView, DeleteView
from .models import Post
from datetime import datetime

class PostsList(ListView):
    model = Post
    ordering = 'time_Post'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = 'обновление по понедельникам'
        return context

class PostsDetal(DeleteView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'