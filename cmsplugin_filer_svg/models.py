# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PageField
from filer.fields.file import FilerFileField
from djangocms_attributes_field.fields import AttributesField

class FilerSVG(CMSPlugin):
    EXCLUDED_KEYS = ['class', 'href', 'target', ]

    image = FilerFileField(null=True, blank=True, default=None, verbose_name=_('image'), on_delete=models.SET_NULL)
    image_url = models.URLField(_('alternative image url'), null=True, blank=True, default=None)
    free_link = models.CharField(_('link'), max_length=2000, blank=True, null=True, help_text=_('if present image will be clickable'))
    page_link = PageField(null=True, blank=True, help_text=_('if present image will be clickable'), verbose_name=_('page link'))
    file_link = FilerFileField(null=True, blank=True, default=None, verbose_name=_('file link'), help_text=_('if present image will be clickable'),
        related_name='+', on_delete=models.SET_NULL)
    original_link = models.BooleanField(_('link original image'), default=False, help_text=_('if present image will be clickable'))
    target_blank = models.BooleanField(_('Open link in new window'), default=False)
    image_classes = models.CharField(max_length=250, verbose_name=_('CSS classes'), null=True, blank=True)
    link_attributes = AttributesField(excluded_keys=EXCLUDED_KEYS, blank=True, help_text=_('Optional. Adds HTML attributes to the rendered link.'))

    @property
    def link(self):
        if self.free_link:
            return self.free_link
        elif self.page_link:
            return self.page_link.get_absolute_url()
        elif self.file_link:
            return self.file_link.url
        elif self.original_link:
            if self.image:
                return self.image.url
            else:
                return self.image_url
        else:
            return ''

    def clean(self):
        from django.core.exceptions import ValidationError
        # Make sure that either image or image_url is set
        if (not self.image and not self.image_url) or (self.image and self.image_url):
            raise ValidationError(_('Either an image or an image url must be selected.'))

    class Meta:
        verbose_name = _('SVG Image')
        verbose_name_plural = _('SVG Images')

    def __unicode__(self):
        if self.image:
            return self.image.label
        else:
            return ''
