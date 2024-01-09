from django.contrib import admin

from lectures.models import Lecture
from common.admin import CKMixin

@admin.register(Lecture)
class CourseAdmin(CKMixin, admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'file', )
