from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    paginator = Paginator(posts, 6)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    context["page"] = page
    return render(request, "note/page_list.html", context=context)

def post_detail(request, post_id):
    context = {}
    post_id = Post.objects.get(id=post_id)
    context["post"] = post_id
    return render(request, 'note/page_detail.html', context=context)

def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('post-detail', post_id=new_post.id)
    
    else:
        post_form = PostForm()
        
    return render(request, 'note/page_form.html', {'form':post_form})

def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
        
    else:
        post_form = PostForm(instance=post)
    return render(request, 'note/page_form.html', {'form':post_form})

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'note/page_confirm_delete.html', {'post':post})