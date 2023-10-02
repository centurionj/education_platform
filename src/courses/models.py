from django.db import models
from autoslug import AutoSlugField

from users.models import Teacher


class Course(models.Model):
    """модель для курсов"""
    title = models.CharField(max_length=255)
    image = models.ImageField('Фотография')
    description = models.TextField('Описание')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    groups = models.ManyToManyField('users.Group', related_name='courses')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    """"модель для категорий курсов"""
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    """модель для лекций в курсе"""
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Текст лекции/ссылка на видео')
    images = models.ManyToManyField('Image', related_name='lectures', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Фотография', upload_to='lecture_images/')
