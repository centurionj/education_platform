from django.conf import settings
from django.db import models


class CourseLike(models.Model):
    """модель понравившихся курсов"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return self.course.name
