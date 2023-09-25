from django.db import models


class RoleStatuses(models.TextChoices):
    TEACHER = 'teacher', 'преподаватель'
    STUDENT = 'student', 'студент'
