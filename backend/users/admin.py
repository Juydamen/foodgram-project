from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name',
                    'last_name', 'email', 'is_subscribed')
    search_fields = ('username',)


admin.site.register(User, UserAdmin)
