from django.contrib import admin

from favourites.models import CourseLike


@admin.register(CourseLike)
class CourseLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', )
