from django.urls import path

from cropimage.views import ImageUploadView


app_name = 'shopifyapp'

urlpatterns = [
    path('upload_image/', ImageUploadView.as_admin_view(), name='upload'),
]