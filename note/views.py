from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from .models import Post
from .forms import PostForm

# Create your views here.
class IndexRedirectView(RedirectView):
    pattern_name = "index"

def info(request):
    return render(request, 'note/info.html')

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-dt_created"]
    paginate_by = 8
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id})
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={"pk":self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse('post-list', kwargs={"pk":self.object.id})
    