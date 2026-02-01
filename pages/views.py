from django.shortcuts import render
from blog.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'pages/home.html', {'posts': posts})

def about(request):
    return render(request, 'pages/about.html')

