from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

class Review(models.Model):
    title = models.CharField('Имя', max_length=20, )
    text = models.TextField('Отзыв',)
    date = models.DateField('Дата публикации',default=timezone.now)
    estimation = models.IntegerField("Оценка", validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

