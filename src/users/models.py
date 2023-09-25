from django.db import models
from django.contrib.auth.models import AbstractUser

from .enums import RoleStatuses


class User(AbstractUser):
    """модель для пользователей"""
    image = models.ImageField('Фотография', upload_to='profile_images/')
    is_verify = models.BooleanField('Подтвержден', default=False)
    phone_number = models.CharField('Телефон', max_length=15, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    grade = models.CharField('Ученая степень', null=True, blank=True)
    role = models.CharField('Роль', choices=RoleStatuses.choices, default=RoleStatuses.STUDENT)

    def __str__(self):
        return self.get_full_name()

    def is_teacher(self):
        return self.role == RoleStatuses.TEACHER

    def is_student(self):
        return self.role == RoleStatuses.STUDENT


class TeacherManager(models.Manager):
    """менеджер объектов преподов"""
    def get_queryset(self):
        return super().get_queryset().filter(role=RoleStatuses.TEACHER)


class StudentManager(models.Manager):
    """менеджер объектов студентов"""
    def get_queryset(self):
        return super().get_queryset().filter(role=RoleStatuses.STUDENT)


class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True


class Group(models.Model):
    """модель группы"""
    title = models.CharField('Название группы', max_length=255)
    students = models.ManyToManyField(Student, related_name='groups')

    def __str__(self):
        return self.title
