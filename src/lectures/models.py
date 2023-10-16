from autoslug import AutoSlugField
from django.db import models

from courses.models import Course


class Lecture(models.Model):
    """Модель для лекций в курсе"""
    title = models.CharField('Название', max_length=255)
    file = models.FileField('PDF', upload_to='lectures/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Лекции'
        verbose_name = 'Лекция'
        ordering = ['course', 'title']

    def __str__(self):
        return self.title
