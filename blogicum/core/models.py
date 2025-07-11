from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class TitleModel(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')

    class Meta:
        abstract = True


class LocationNameModel(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        abstract = True
