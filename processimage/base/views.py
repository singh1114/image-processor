from abc import ABCMeta, abstractmethod

from django.contrib import admin
from django.views import View


class AbstractAdminBaseView(View, metaclass=ABCMeta):

    @classmethod
    def as_admin_view(cls):
        view = cls.as_view()
        admin_site = admin.site
        return admin_site.admin_view(view)

    @property
    @abstractmethod
    def template(self):
        return NotImplementedError('Abstract method template not defined.')
