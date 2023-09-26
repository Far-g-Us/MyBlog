from django.db import models
from django.contrib.auth.models import User
class Arta(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    desc = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='home/image/')
    date = models.DateField('Дата')
    url = models.URLField('Доп. источник', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f"{self.title} | {self.date} | {self.desc.max_length:50}"

