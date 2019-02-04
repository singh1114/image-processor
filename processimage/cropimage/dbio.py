from base.dbio import BaseDbIO

from cropimage.models import ImageModel


class ImageModelDbIO(BaseDbIO):

    @property
    def model(self):
        return ImageModel
