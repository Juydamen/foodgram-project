from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):            # Модель для пользователя
    # электронная почта
    email = models.EmailField(max_length=254,
                              unique=True,
                              blank=False,
                              null=False)
    # имя пользователя
    username = models.CharField(max_length=20,
                                unique=True,
                                blank=False,
                                null=False)
    # имя
    first_name = models.CharField(max_length=150,
                                  blank=False,
                                  null=False)
    # фамилия
    last_name = models.CharField(max_length=150,
                                 blank=False,
                                 null=False)
    # есть ли подписка на кого-то
    password = models.CharField(max_length=150,
                                blank=False,
                                null=False,)
    # подписан кто то на пользователя или не
    is_subscribed = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'               # удобочитаемое имя модели
        verbose_name_plural = 'Пользователи'        # переименовать в админке

    def __str__(self):
        return self.username


class Subscription(models.Model):    # Модель для подписчика
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Пользователь')

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='following',
                               verbose_name='Автор')

    class Meta:
        models.UniqueConstraint(
            fields=['user', 'author'],              #
            name='unique_Subscription'              #
        )
        verbose_name = 'Подписка'                   # удобочитаемое имя модели
        verbose_name_plural = 'Подписки'            # переименовать в админке

    def __str__(self):
        return f'{self.user.username} подписан на {self.author.username}'
