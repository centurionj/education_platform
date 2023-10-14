from django.contrib import admin

from .models import Lecture


@admin.register(Lecture)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file', )
