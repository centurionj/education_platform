from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from users.models import Groups, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'username', 'role', 'grade',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'groups', 'grade')}),
        (_('Permissions'), {'fields': ('is_active', 'role',), }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')


@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.unregister(Group)
