# -*- coding: utf-8 -*-
from django import forms
from djangocms_attributes_field.widgets import AttributesWidget
from .models import FilerSVG
import os

class FilerSVGForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilerSVGForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()

    def clean(self):
        image = self.cleaned_data.get('image')
        if image:
            url = image.url
        else:
            url = self.cleaned_data.get('image_url')

        ext = os.path.splitext(url)[1].lower()
        if ext not in ['.svg']:
            raise forms.ValidationError('Invalid file type')

    class Meta:
        model = FilerSVG
        exclude = []
