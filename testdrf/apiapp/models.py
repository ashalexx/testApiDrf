from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(verbose_name='Продукт', max_length=255)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.CASCADE)
    # can_view = models.BooleanField(default=False)  # Флаг, позволяющий просматривать продукт
    # can_edit = models.BooleanField(default=False)  # Флаг, позволяющий редактировать продукт
    # can_delete = models.BooleanField(default=False)  # Флаг, позволяющий удалять продукт


class Lesson(models.Model):
    name = models.CharField(verbose_name='Название урока', max_length=255)
    video_link = models.URLField(verbose_name='Ссылка на видео')
    duration = models.IntegerField(verbose_name='Длительность видео')
    products = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LessonView(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', verbose_name='Урок', on_delete=models.CASCADE)
    viewed_time = models.IntegerField(verbose_name='Сколько видео просмотрено', )
    status = models.BooleanField(verbose_name='Просмотрено/Не просмотрено', default=False)

    def save(self, *args, **kwargs):
        if self.viewed_time >= 0.8 * self.lesson.duration:
            self.status = True
        else:
            self.status = False
        super().save(*args, **kwargs)

