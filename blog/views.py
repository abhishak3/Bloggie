from django.views.generic import ListView, DetailView

from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'all_posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

