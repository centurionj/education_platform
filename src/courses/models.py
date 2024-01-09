from PIL import Image
from autoslug import AutoSlugField
from django.db import models


from users.models import User
from users.enums import RoleStatuses

class Course(models.Model):
    """модель для программы обучения"""
    title = models.CharField('Название', max_length=255)
    image = models.ImageField('Фотография', upload_to='courses_images/')
    description = models.TextField('Описание')
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Преподаватель",
        limit_choices_to={'role': RoleStatuses.TEACHER},
        related_name="teacher_course",
    )
    student_group = models.ForeignKey('users.StudentGroup', related_name='user_group', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            image = Image.open(self.image.path)
            image.thumbnail((600, 450))
            image.save(self.image.path)

    class Meta:
        verbose_name_plural = 'Программы обучения'
        verbose_name = 'Программа обучения'
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    """"модель для категорий курсов"""
    title = models.CharField('Название', max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['title']

    def __str__(self):
        return self.title
