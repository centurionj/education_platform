from django.conf import settings
from django.db import models


class CourseLikeManager(models.Manager):
    """Менеджер для собственного метода добавления или удаления в лайк"""
    def delete_or_create(self, user, course_id):
        course, created = self.get_or_create(user=user, course_id=course_id)

        if not created:
            course.delete()

        return course


class CourseLike(models.Model):
    """модель понравившихся курсов"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    objects = CourseLikeManager()

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return self.course.title
