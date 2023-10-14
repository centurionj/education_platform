from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = models.TextField('Контент')
    file = models.FileField('Фото', upload_to='news_images')
    datetime = models.DateTimeField('Дата', auto_now=True)

    def __str__(self):
        return self.title
