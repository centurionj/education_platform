from django.contrib import admin

from users.models import Group, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'username',  'role', 'grade')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
