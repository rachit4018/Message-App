from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'Home.html'
    context_object_name = 'all_posts_list'
