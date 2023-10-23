from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Answer, Question, Test, TestResult


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 4


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]


@admin.register(Test)
class TestAdmin(NestedModelAdmin):
    model = Test
    inlines = [QuestionInline]


@admin.register(TestResult)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'score')
