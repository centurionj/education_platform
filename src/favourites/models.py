from django.conf import settings
from django.db import models


class CourseLike(models.Model):
    """модель понравившихся курсов"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    @classmethod
    def update_or_create(cls, user, course_id):
        """Добавление удаление курсов из лайка"""
        course = CourseLike.objects.filter(user=user, course_id=course_id)

        if not course.exists():
            obj = CourseLike.objects.create(user=user, course_id=course_id)
            return obj
        else:
            obj = CourseLike.objects.get(user=user, course_id=course_id)
            obj.delete()
            return obj

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return self.course.title
