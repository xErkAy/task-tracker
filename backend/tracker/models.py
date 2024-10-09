from django.db import models

from account.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Task(models.Model):
    class Status(models.IntegerChoices):
        not_started = 1, 'Не начата'
        in_analysis = 2, 'В анализе'
        in_progress = 3, 'В работе'
        closed = 4, 'Завершена'

    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Создатель', related_name='created_tasks')
    performer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Исполнитель', related_name='tasks')

    due_date = models.DateField(verbose_name='Срок исполнения', null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.not_started, verbose_name='Статус')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return f'{self.name} {self.performer.full_name} - {self.due_date}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
