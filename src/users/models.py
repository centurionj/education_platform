from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from .enums import RoleStatuses


class User(AbstractUser):
    """Модель для пользователей"""
    image = models.ImageField('Фотография', upload_to='profile_images/', null=True, blank=True)
    is_verify = models.BooleanField('Подтвержден', default=False)
    phone_number = models.CharField('Телефон', max_length=15, null=True, blank=True)
    student_group = models.ForeignKey(
        'users.StudentGroup',
        related_name='students',
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    description = models.TextField('Описание', null=True, blank=True)
    grade = models.CharField('Ученая степень', max_length=50, null=True, blank=True)
    role = models.CharField('Роль', max_length=50, choices=RoleStatuses.choices, default=RoleStatuses.STUDENT)

    def is_teacher(self):
        return self.role == RoleStatuses.TEACHER

    def is_student(self):
        return self.role == RoleStatuses.STUDENT

    def is_admin(self):
        return self.role == RoleStatuses.ADMIN

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['last_name', 'first_name', 'role']


    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if self.is_teacher():
            self.is_staff = True
            self.is_superuser = False
            self.is_verify = True

        if self.is_superuser:
            self.is_staff = True
            self.is_verify = True
            self.role = RoleStatuses.ADMIN

        super(User, self).save(*args, **kwargs)


# class Teacher(User):
#     description = models.TextField('Описание', null=True, blank=True)
#     grade = models.CharField('Ученая степень', max_length=50, null=True, blank=True)
#
#     class Meta:
#         verbose_name_plural = 'Преподаватели'
#         verbose_name = 'Преподаватель'
#         ordering = ['last_name', 'first_name']
#
#
# class Student(User):
#     student_group = models.ForeignKey(
#         'users.StudentGroup',
#         related_name='students',
#         null=True, blank=True,
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#         verbose_name_plural = 'Студенты'
#         verbose_name = 'Студент'
#         ordering = ['last_name', 'first_name']


class StudentGroup(models.Model):
    """модель группы"""
    title = models.CharField('Название группы', max_length=255)

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = ['title']

    def __str__(self):
        return self.title
