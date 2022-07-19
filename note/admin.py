from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import Post, User, Comment, Like


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    
    
class LikeInline(GenericStackedInline):
    model = Like   
    
class UserInline(admin.StackedInline):
    model = User.following.through
    fk_name = "to_user"
    verbose_name = "Followers"
    verbose_name_plural = "Followers"
    
    
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "profile_pic", "intro", "following",)}), )
UserAdmin.inlines = (UserInline, )

class PostAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
        LikeInline,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInline,
    )


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)


