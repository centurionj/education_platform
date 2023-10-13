from autoslug import AutoSlugField
from django.db import models

from courses.models import Course


class LectureTitle(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)


class LectureContent(models.Model):
    content = models.TextField('Контент')
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)


class LectureImage(models.Model):
    image = models.ImageField('Фотография', upload_to='lecture_images/')
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)


class Lecture(models.Model):
    """Модель для лекций в курсе"""
    title = models.ManyToManyField(LectureTitle, related_name='lectures')
    content = models.ManyToManyField(LectureContent, related_name='lectures')
    images = models.ManyToManyField(LectureImage, related_name='lectures', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title
