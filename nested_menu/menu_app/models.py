from django.db import models


class Menu(models.Model):
    title = models.CharField(
        'Название меню',
        max_length=50
    )
    slug = models.SlugField(
        'Имя для template tag',
        max_length=250,
        blank=True,
        null=True,
        help_text='Имя для вызова через template tag'
        )
    url = models.CharField(
        'Ссылка',
        max_length=250,
        blank=True,
        null=True,
        help_text='url name в модуле urls.py'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    
    def get_url(self):
        if self.url:
            url = self.url
        else:
            url = '/'
        return url
    
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
        verbose_name='Дочерний элемент',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        'Название элемента',
        max_length=100,
    )
    url = models.CharField(
        'Ссылка',
        max_length=250,
        blank=True,
        help_text='url name в модуле urls.py'
    )
    
    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def get_url(self):
        if self.url:
            url = self.url
        else:
            url = '/'
        return url

    def __str__(self):
        return self.title


