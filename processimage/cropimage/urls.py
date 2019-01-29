from django.urls import path

from cropimage.views import (
    ImageUploadView,
    ShowMainImagesView,
    ShowCroppedImagesView
)


app_name = 'cropimage'

urlpatterns = [
    path('upload_image/', ImageUploadView.as_admin_view(), name='upload'),
    path('show_main_images/',
         ShowMainImagesView.as_admin_view(), name='show_main_image'),
    path('show_cropped_images/<uuid:main_image_uuid>',
         ShowCroppedImagesView.as_admin_view(), name='show_cropped_images'),
]