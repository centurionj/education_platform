from django.db import models


class RoleStatuses(models.TextChoices):
    """Статусы для юзеров"""
    TEACHER = 'teacher', 'преподаватель'
    STUDENT = 'student', 'студент'
    ADMIN = 'admin', 'администратор'
