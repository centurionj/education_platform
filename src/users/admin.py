from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import StudentGroup, User
from common.admin import ImagePreviewMixin

@admin.register(User)
class UserAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_verify', 'phone_number', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': (
            'image',
            'image_preview',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_verify',
            'student_group',
            'description',
            'grade',
            'role'
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['image_preview']

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin, ImagePreviewMixin):
#     list_display = ('first_name', 'last_name', 'grade')
#     search_fields = ('first_name', 'last_name', 'email')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': (
#             'image',
#             'image_preview',
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'description',
#             'grade',
#             'is_verify',
#             'role'
#         )}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     readonly_fields = ['image_preview']
#
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin, ImagePreviewMixin):
#     list_display = ('first_name', 'last_name', 'student_group')
#     search_fields = ('first_name', 'last_name', 'email', 'student_group')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': (
#             'image',
#             'image_preview',
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'student_group',
#             'is_verify',
#             'role'
#         )}),
#     )
#     readonly_fields = ['image_preview']

@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.unregister(Group)
