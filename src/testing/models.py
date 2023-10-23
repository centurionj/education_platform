from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models

from courses.models import Course
from users.models import Group


class Test(models.Model):
    name = models.CharField('Название', max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='testing', null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'
        ordering = ['name']

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField('Текст вопроса')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['test', 'text']

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField('Ответ', max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'
        ordering = ['question', 'text']

    def __str__(self):
        return self.text


class TestResult(models.Model):
    user = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField('Количество баллов', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'Результаты'
        verbose_name = 'Результат'
        ordering = ['user', 'test']

    def __str__(self):
        return self.user.get_full_name()
