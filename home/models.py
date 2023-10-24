from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Категория', max_length=35)

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=50, null=True)
    desc = models.TextField('Описание', max_length=120, null=True)
    image = models.ImageField('Изображение', upload_to='home/image/')
    date = models.DateField('Дата')
    content = models.TextField('Содержание статьи', null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    # url = models.URLField('Доп. источник', blank=True)
    #
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    #
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title} | {self.date}'


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'