from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'note/index.html')

def info(request):
    return render(request, 'note/info.html')

def post_list(request):
    context = {}
    posts = Post.objects.all()
    context["posts"] = posts
    
    return render(request, "note/page_list.html", context=context)

def post_detail(request, post_id):
    context = {}
    post_id = Post.objects.get(id=post_id)
    context["post"] = post_id
    return render(request, 'note/page_detail.html', context=context)