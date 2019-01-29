from PIL import Image

from cropimage.choices import ImageType
from cropimage.models import ImageModel


class CropImageHandler:

    def __init__(self, model_obj):
        self.image_obj = model_obj

    def crop_images(self):
        base_image = Image.open(self.image_obj.image._file.name)
        self.create_horizontal_image(base_image)
        self.create_vertical_image(base_image)
        self.create_horizontal_small_image(base_image)
        self.create_gallery_image(base_image)

    def create_horizontal_image(self, base_image):
        horizontal_area = (0, 0, 755, 450)
        ImageModel.objects.create(
            parent_image=self.image_obj,
            image=self.create_cropped_image(base_image, horizontal_area),
            image_type=ImageType.HORIZONTAL_IMAGE
        )

    def create_vertical_image(self, base_image):
        vertical_area = (0, 0, 365, 450)
        ImageModel.objects.create(
            parent_image=self.image_obj,
            image=self.create_cropped_image(base_image, vertical_area),
            image_type=ImageType.VERTICAL_IMAGE
        )

    def create_horizontal_small_image(self, base_image):
        horizontal_small_area = (0, 0, 365, 212)
        ImageModel.objects.create(
            parent_image=self.image_obj,
            image=self.create_cropped_image(base_image, horizontal_small_area),
            image_type=ImageType.HORIZONTAL_SMALL_IMAGE
        )

    def create_gallery_image(self, base_image):
        gallery_area = (0, 0, 380, 380)
        ImageModel.objects.create(
            parent_image=self.image_obj,
            image=self.create_cropped_image(base_image, gallery_area),
            image_type=ImageType.GALLERY_IMAGE
        )

    def create_cropped_image(self, base_image, area):
        full_path_name = self.create_fullpath_name(base_image.filename, area)
        base_image.crop(area).save(full_path_name)
        return self.create_relative_path(full_path_name)

    def create_fullpath_name(self, filename, area):
        path_list = filename.split('/')
        last_path = ''.join([str(a) for a in area]) + path_list[-1]
        return '/'.join(path_list[:-1] + [last_path])

    def create_relative_path(self, full_path_name):
        return '/'.join(full_path_name.split('/')[-2:])

