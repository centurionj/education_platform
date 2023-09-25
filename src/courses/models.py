from django.db import models
from users.models import Teacher


class Course(models.Model):
    """модель для курсов"""
    title = models.CharField(max_length=255)
    image = models.ImageField('Фотография', upload_to='course_images/')
    description = models.TextField('Описание')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    groups = models.ManyToManyField('users.Group', related_name='courses')

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Текст лекции/ссылка на видео')
    images = models.ManyToManyField('Фотографии', related_name='lectures', upload_to='lecture_images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Фотография', upload_to='lecture_images/')
