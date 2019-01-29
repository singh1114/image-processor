from django import forms

from cropimage.choices import ImageType
from cropimage.models import ImageModel


class ImageUploadForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = ImageModel
        fields = ('image',)

    def clean_image(self):
        """Validate if the image size is 1024 X 1024."""
        image = self.cleaned_data['image']
        self.cleaned_data['image_type'] = ImageType.MAIN_IMAGE
        width = image.image.width
        height = image.image.height
        if width == 1024 and height == 1024:
            return image
        raise forms.ValidationError('Image should be of size 1024 X 1024.')
