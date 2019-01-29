from django.contrib import admin

from base.admin import BaseAdmin

from cropimage.models import ImageModel


@admin.register(ImageModel)
class ImageModelAdmin(BaseAdmin):
    readonly_fields = ('parent_image', 'created_at')
    list_display = ('uuid', 'image_type', 'image_width', 'image_height')
