from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Контент')
    file = models.FileField('Фото', upload_to='news_images')
    datetime = models.DateTimeField('Дата', auto_now=True)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['datetime', 'title']

    def __str__(self):
        return self.title
