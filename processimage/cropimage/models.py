from django.db import models

from base.models import AbstractBaseModel

from cropimage.choices import (
    IMAGE_TYPE_CHOICES,
    ImageType
)


class ImageModel(AbstractBaseModel):
    parent_image = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    image_type = models.IntegerField(
        choices=IMAGE_TYPE_CHOICES,
        default=ImageType.MAIN_IMAGE)
    image = models.ImageField(
        upload_to='images/', width_field='image_width',
        height_field='image_height')
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
