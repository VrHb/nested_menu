from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.DO_NOTHING,
    )
