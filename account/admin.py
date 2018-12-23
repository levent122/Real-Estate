from django.contrib import admin
from .models import UserInfo, Like


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    class Meta:
        model = UserInfo



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']
    class meta:
        model = Like