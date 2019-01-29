from cropimage.choices import ImageType
from cropimage.models import ImageModel


class ShowImageHandler:

    def get_all_main_images(self):
        return ImageModel.objects.filter(image_type=ImageType.MAIN_IMAGE)

    def get_all_child_images(self, main_image_uuid):
        image_data_list = []
        images = ImageModel.objects.filter(parent_image__uuid=main_image_uuid)
        for image in images:
            image_data_list.append({
                'image': image,
                'image_type': image.get_image_type_display()
            })
        return image_data_list
