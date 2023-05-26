from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # Модель для пользователя
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_subscribed = models.BooleanField(default=False)

    # REQUIRED_FIELDS = ['first_name', 'last_name', 'is_subscribed']
    # USERNAME_FIELD = ['email']
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Follow(models.Model):  # Модель для подписчика
    user = models.ForeignKey(User,
                             related_name='user',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               related_name='follow',
                               on_delete=models.CASCADE)

    class Meta:
        models.UniqueConstraint(
            fields=['user', 'author'],
            name='unique_following'
        )
