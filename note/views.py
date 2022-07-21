from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.contrib.contenttypes.models import ContentType
from braces.views import LoginRequiredMixin
from allauth.account.views import PasswordChangeView
from .models import Post, User, Comment, Like
from .forms import PostForm, ProfileForm, CommentForm
from .mixin import LoginAndVerificationRequiredMixin, LoginAndOwershipRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'note/index.html')

def info(request):
    return render(request, 'note/info.html')

# Post
class PostListView(ListView):
    model = Post
    ordering = ["-dt_created"]
    paginate_by = 8
    
class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["post_content_type_id"] = ContentType.objects.get(model='post').id
        context["comment_content_type_id"] = ContentType.objects.get(model='comment').id
        
        user = self.request.user
        if user.is_authenticated:
            post = self.get_object()
            context["likes_post"] = Like.objects.filter(user=user, post=post).exists()
            context["likes_comment"] = Comment.objects.filter(post=post).filter(likes__user=user)
        return context

class PostCreateView(LoginAndVerificationRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id})
    
    
class PostUpdateView(LoginAndOwershipRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={"pk":self.object.id})
    

class PostDeleteView(LoginAndOwershipRequiredMixin, DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse('post-list')

# Profile
class UserPostListView(ListView):
    model = Post
    template_name = "note/user_post_list.html"
    context_object_name = "user_posts"
    paginate_by = 2
    
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Post.objects.filter(author__id=user_id).order_by("-dt_created")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context

class ProfileView(DetailView):
    model = User
    template_name = "note/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        context["user_post"] = Post.objects.filter(author__id=user_id).order_by("-dt_created")[:2]
        context["posts"] = Post.objects.filter(author__id=user_id).order_by("-dt_created").count()
        return context


class ProfileUpdateForm(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "note/profile_update_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse('profile', kwargs=({"user_id":self.request.user.id}))

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('post-list')

# Comment
class CommentCreateView(LoginAndVerificationRequiredMixin, CreateView):
    http_method_names = ["post"]
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get("pk"))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk":self.kwargs.get("pk")})

class CommentUpdateView(LoginAndOwershipRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "note/comment_update_form.html"
    pk_url_kwarg = "comment_id"
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={"pk":self.object.post.id})
    

class CommentDeleteView(LoginAndOwershipRequiredMixin, DeleteView):
    model = Comment
    pk_url_kwarg = "comment_id"
    template_name = "note/comment_confirm_delete.html"
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={"pk":self.object.post.id})

# Like
class ProcessLikeView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, reqeust, *args, **kwargs):
        like, created = Like.objects.get_or_create(
            user = self.request.user,
            content_type_id = self.kwargs.get("content_type_id"),
            object_id = self.kwargs.get("object_id"),
        )
        
        if not created:
            like.delete()
        
        return redirect(self.request.META["HTTP_REFERER"])
            