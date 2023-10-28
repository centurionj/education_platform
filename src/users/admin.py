from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from users.models import StudentGroups, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'username', 'role', 'grade',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'student_groups', 'grade')}),
        (_('Permissions'), {'fields': ('is_active', 'role', 'groups'), }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')
    # filter_horizontal = ('student_groups',)


@admin.register(StudentGroups)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.unregister(Group)
