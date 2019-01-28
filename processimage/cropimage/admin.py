from django.contrib import admin

from base.admin import BaseAdmin

from cropimage.models import ImageModel


@admin.register(ImageModel)
class ImageModelAdmin(BaseAdmin):
    pass
