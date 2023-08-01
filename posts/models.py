from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class Post(models.Model):

    def __str__(self):
        return f'{self.author}\n{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, verbose_name='post author')
    title = models.CharField(max_length=100, verbose_name='post title')
    body = models.TextField(max_length=2000, verbose_name='post body')
