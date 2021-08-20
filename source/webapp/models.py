from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


class Advert(models.Model):
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='Description'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        related_name='adverts',
        verbose_name='Author'
    )
    phone_number = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name='Phone Number'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        db_table = 'adverts'
        verbose_name = 'Advert'
        verbose_name_plural = 'Adverts'

    def __str__(self):
        return f'{self.author} - {self.phone_number}'


class Image(models.Model):
    advert = models.ForeignKey(
        'webapp.Advert',
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='adverts',
        verbose_name='Author'
    )
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to='images',
        verbose_name='Image'
    )

    class Meta:
        db_table = 'images'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.advert} - {self.image}'





