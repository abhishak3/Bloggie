from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy

from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'all_posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__' # all fields of model Post

class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text'] # we don't want author to change

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home') # redirects only when deletion is completed

