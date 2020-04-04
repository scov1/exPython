from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Car(models.Model):
    name = models.CharField('Марка машины', max_length=100)
    model = models.CharField('Модель машины', max_length=100)
    img = models.ImageField(upload_to='img', blank=True, verbose_name='Изображение')
    desc = models.TextField('Описание')
    price = models.IntegerField('Цена', null=False)
    offer = models.BooleanField(default=False)
    public_date = models.DateTimeField('Дата публикации')
    year = models.IntegerField('Год выпуска', null=False)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    comment_author_name = models.CharField('Имя', max_length=50)
    comment_text = models.TextField('Текст комментария')

    def __str__(self):
        return self.comment_author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    ava = models.ImageField("Фото", upload_to="img", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=20)
    adress = models.CharField("Адрес", max_length=250)
    slug = models.SlugField("URL", max_length=50, default='')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
