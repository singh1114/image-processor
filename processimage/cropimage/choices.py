class ImageType:
    MAIN_IMAGE = 0
    HORIZONTAL_IMAGE = 1
    VERTICAL_IMAGE = 2
    HORIZONTAL_SMALL_IMAGE = 3
    GALLERY_IMAGE = 4


IMAGE_TYPE_CHOICES = (
    (ImageType.MAIN_IMAGE, 'Main Image'),
    (ImageType.HORIZONTAL_IMAGE, 'Horizontal Image'),
    (ImageType.VERTICAL_IMAGE, 'Vertical Image'),
    (ImageType.HORIZONTAL_SMALL_IMAGE, 'Horizontal Small Image'),
    (ImageType.GALLERY_IMAGE, 'Gallery Image')
)
