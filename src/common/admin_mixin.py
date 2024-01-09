from django.utils.safestring import mark_safe
from django.db import models

from ckeditor.widgets import CKEditorWidget

class ImagePreviewMixin:
    """Миксин для отображения картинок в админке"""
    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    image_preview.short_description = 'Фотография предпросмотр'


class CKMixin:
    """Миксин для текстового редактора в админке"""
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
