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

    def post(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # import ipdb; ipdb.set_trace()
            form.save()
        else:
            return render(
                request,
                self.template,
                {
                    'message': form.errors
                })
        return render(
            request,
            self.template,
            {
                'form': ImageUploadForm()
            })
