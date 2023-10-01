from django.db import models
from autoslug import AutoSlugField

from courses.models import Course
from users.models import Group


class Test(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='testing')
    slug = AutoSlugField(populate_from='name', unique=True, editable=False)


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


class TestResult(models.Model):
    user = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()