from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from slugify import slugify

from obj_ev.models import ObjEv
from users.models import Userc

from io import BytesIO

from PIL import Image
from django.core.files import File


class Stat(models.Model):
    """model for posts"""
    domen = models.ForeignKey(ObjEv, related_name='stat_domen', on_delete=models.CASCADE, verbose_name='Domen',
                               default=None, blank=True, null=True)
    Uin = models.CharField(max_length=255, default=None)
    Uout = models.CharField(max_length=255, default=None)
    temp = models.CharField(max_length=255, default=None)
    voltage = models.CharField(max_length=255, default=None)
    date = models.DateTimeField(auto_now_add=True, editable=False,unique=True,)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    def __str__(self):
        return str(self.date)[:-13]

    def get_absolute_url(self):
        return reverse('poster', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('edit', kwargs={'slug': self.slug})

    def get_absolute_url_del(self):
        return reverse('delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.date)[:-13])
        super(Stat, self).save(*args, **kwargs)



