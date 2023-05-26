from django.contrib import admin
from users.models import User, Follow


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name',
                    'last_name', 'email', 'is_subscribed')
    search_fields = ('username',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('author',)


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
