import shutil

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from slugify import slugify
from django.utils.translation import ugettext_lazy as _

from io import BytesIO

from PIL import Image
from django.core.files import File
from obj_ev.models import ObjEv
from frag import settings


class Userc(AbstractUser):
    """model for users"""

    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    objs = models.ManyToManyField(ObjEv,related_name="users_domen", blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username.lower())
        super(Userc, self).save(*args, **kwargs)


