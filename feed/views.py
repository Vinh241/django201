from django.views.generic import ListView
from .models import Post

class HomePage(ListView):
    template_name='feed/homepage.html'
    http_method_names = ['get']
    model= Post
    context_object_name='posts'
    queryset = Post.objects.all().order_by('-id')[0:30]