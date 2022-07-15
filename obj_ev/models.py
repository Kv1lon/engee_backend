from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.db import models
from slugify import slugify


class ObjEv(models.Model):
    """model for countries"""
    title = models.CharField(max_length=255)
    alarm = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # call the compress function
        # set self.image to new_image
        self.slug = (slugify(self.title))

        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('country_profile', kwargs={'slug': self.slug})
