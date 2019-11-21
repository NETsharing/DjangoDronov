from  django.db import models
from django.core import validators
from django.contrib.auth.models import User
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', unique=True,
                             validators=[validators.RegexValidator(regex='^.{4,}$')],
                             error_messages={'invalid': 'Направильное название товара'})
    content = models.TextField(null=True, verbose_name='Текст объявления', blank=True, editable=True)
    price = models.FloatField (null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete = models.PROTECT, verbose_name='Рубрика', related_name='entries')
    moderator = models.ForeignKey('Moderator', null=True, on_delete=models.PROTECT)

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValueError('Укажите описание товара')
        if self.price < 0:
            errors['price'] = ValueError('Цена не может быть отрицательна')
        if errors:
            raise ValueError(errors)
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        unique_together = (('title', 'published'), ('title', 'price', 'rubric'))
        ordering = ['-published', 'title']
        # order_with_respect_to = 'rubric'

class Rubric(models.Model):
    name = models.CharField(max_length=20, null=True, verbose_name='Рубрика')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Moderator(models.Model):
    nameMod = models.CharField(max_length=20, null=True,  verbose_name='Модератор')
    def __str__(self):
        return self.nameMod
class TypeModeration(models.Model):
    # name = models.CharField(max_length=20)
    types = models.ManyToManyField(Moderator, null=True, verbose_name='Тип модераций')
    # def __str__(self):
    #     return self.name

