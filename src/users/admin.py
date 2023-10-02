from django.contrib import admin

from users.models import User, Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'grade', 'role')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
