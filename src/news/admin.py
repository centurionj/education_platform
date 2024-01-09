from django.contrib import admin

from news.models import News
from common.admin_mixin import CKMixin, ImagePreviewMixin

@admin.register(News)
class NewsAdmin(CKMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'datetime',)
    fields = [
        'image',
        'image_preview',
        'title',
        'content',
    ]
    readonly_fields = ['image_preview']
