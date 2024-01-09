from django.contrib import admin

from courses.models import Category, Course
from common.admin_mixin import CKMixin, ImagePreviewMixin


@admin.register(Course)
class CourseAdmin(CKMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher', 'category',)
    fields = [
        'image',
        'image_preview',
        'title',
        'description',
        'teacher',
        'student_group',
        'category',
    ]
    readonly_fields = ['image_preview']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
