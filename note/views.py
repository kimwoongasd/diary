from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'note/index.html')

def post_list(request):
    context = {}
    posts = Post.objects.all()
    context["posts"] = posts
    
    return render(request, "note/page_list.html", context=context)