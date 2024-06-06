from django.db import models
from django.utils import timezone

class Workers(models.Model):
    title = models.CharField('Имя', max_length=40)
    text = models.TextField('Описание работника')
    main = models.ImageField(upload_to='images/')
    left = models.ImageField(upload_to='images/', default='path/to/my/default/image.jpg')
    right = models.ImageField(upload_to='images/', default='path/to/my/default/image.jpg')
    birthday = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'Работника'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField('Название услуги', max_length=40)
    text = models.TextField('Описание услуги')
    main = models.ImageField(upload_to='images/')
    left = models.ImageField(upload_to='images/', default='path/to/my/default/image.jpg')
    right = models.ImageField(upload_to='images/', default='path/to/my/default/image.jpg')
    prise = models.TextField('Стоимость')
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Работник', related_name='services',
                               null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
