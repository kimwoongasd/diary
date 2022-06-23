from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

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

def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        new_post = post_form.save()
        return redirect('post-detail', post_id=new_post.id)
    else:
        post_form = PostForm()
        return render(request, 'note/page_form.html', {'form':post_form})