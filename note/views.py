from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from allauth.account.views import PasswordChangeView
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'note/index.html')

def info(request):
    return render(request, 'note/info.html')

def profile(request):
    return render(request, 'note/profile.html')

class PostListView(ListView):
    model = Post
    ordering = ["-dt_created"]
    paginate_by = 8
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
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
        return reverse('post-list')
    
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('post-list')
    