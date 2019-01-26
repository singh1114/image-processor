from django.shortcuts import render

from base.views import AbstractAdminBaseView

from cropimage.forms import ImageUploadForm


class ImageUploadView(AbstractAdminBaseView):

    @property
    def template(self):
        return 'cropimage/image_upload.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template,
            {
                'form': ImageUploadForm()
            })
