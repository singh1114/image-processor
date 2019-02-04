import os

from io import BytesIO

from PIL import Image

from base.utils import get_joined_path, upload_image

from cropimage.choices import ImageType
from cropimage.dbio import ImageModelDbIO


class CropImageHandler:

    def __init__(self, model_obj):
        self.image_obj = model_obj

    def crop_images(self):
        self.create_horizontal_image_obj()
        self.create_vertical_image_obj()
        self.create_horizontal_small_image_obj()
        self.create_gallery_image_obj()

    def create_horizontal_image_obj(self):
        base_image = Image.open(self.image_obj.image.file)
        horizontal_area = (0, 0, 755, 450)
        ImageModelDbIO().create_object({
            'parent_image': self.image_obj,
            'image': self.create_cropped_image(base_image, horizontal_area),
            'image_type': ImageType.HORIZONTAL_IMAGE
        })

    def create_vertical_image_obj(self):
        base_image = Image.open(self.image_obj.image.file)
        vertical_area = (0, 0, 365, 450)
        ImageModelDbIO().create_object({
            'parent_image': self.image_obj,
            'image': self.create_cropped_image(base_image, vertical_area),
            'image_type': ImageType.VERTICAL_IMAGE
        })

    def create_horizontal_small_image_obj(self):
        base_image = Image.open(self.image_obj.image.file)
        horizontal_small_area = (0, 0, 365, 212)
        ImageModelDbIO().create_object({
            'parent_image': self.image_obj,
            'image': self.create_cropped_image(
                base_image, horizontal_small_area),
            'image_type': ImageType.HORIZONTAL_SMALL_IMAGE
        })

    def create_gallery_image_obj(self):
        base_image = Image.open(self.image_obj.image.file)
        gallery_area = (0, 0, 380, 380)
        ImageModelDbIO().create_object({
            'parent_image': self.image_obj,
            'image': self.create_cropped_image(base_image, gallery_area),
            'image_type': ImageType.GALLERY_IMAGE
        })

    def create_cropped_image(self, base_image, area):
        full_path_name = self.create_image_fullpath_name(base_image.fp.name, area)
        stream = BytesIO()
        new_image = base_image.crop(area)
        new_image.save(stream, 'PNG')
        return upload_image(stream, full_path_name)

    def create_image_fullpath_name(self, filename, area):
        full_path = os.path.split(filename)
        new_image_path = ''.join([str(a) for a in area]) + full_path[-1]
        return get_joined_path(full_path[:-1], new_image_path)
