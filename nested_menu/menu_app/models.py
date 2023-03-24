from django.db import models


class Menu(models.Model):
    title = models.CharField('Название меню', max_length=50)
    slug = models.SlugField(
        'Часть меню для url',
        max_length=250,
        blank=True,
        null=True
        )
    url = models.CharField(
        'Имя url',
        max_length=250,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    
    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        verbose_name='Меню',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        related_name='items',
        verbose_name='Родительский элемент',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        'Название элемента',
        max_length=100,
    )
    url = models.CharField(
        'Ссылка',
        max_length=250,
        blank=True
    )
    
    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.title


