from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, User
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "profile_pic")}), )