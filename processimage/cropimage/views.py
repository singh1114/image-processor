from django.shortcuts import render

from base.views import AbstractAdminBaseView

from cropimage.forms import ImageUploadForm
from cropimage.handlers.crop_image_handler import CropImageHandler
from cropimage.handlers.show_image_handler import ShowImageHandler


class ImageUploadView(AbstractAdminBaseView):

    @property
    def template(self):
        return 'cropimage/upload_image.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template,
            {
                'form': ImageUploadForm()
            })

    def post(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model_obj = form.save()
            CropImageHandler(model_obj).crop_images()
        else:
            return render(request, self.template, {'message': form.errors})
        return render(request, self.template, {
            'message': 'Image uploaded successfully!'})


class ShowMainImagesView(AbstractAdminBaseView):

    @property
    def template(self):
        return 'cropimage/show_main_image.html'

    def get(self, request, *args, **kwargs):
        images = ShowImageHandler().get_all_main_images()
        return render(request, self.template, {'images': images})


class ShowCroppedImagesView(AbstractAdminBaseView):

    @property
    def template(self):
        return 'cropimage/show_all_images.html'

    def get(self, request, main_image_uuid, *args, **kwargs):
        images = ShowImageHandler().get_all_child_images(main_image_uuid)
        return render(request, self.template, {'images': images})
