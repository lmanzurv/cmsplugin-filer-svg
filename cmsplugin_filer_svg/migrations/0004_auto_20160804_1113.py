# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion
import cms.models.fields
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0006_auto_20160623_1627'),
        ('cmsplugin_filer_svg', '0003_auto_20160706_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='filersvg',
            name='file_link',
            field=filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, default=None, to='filer.File', blank=True, help_text='if present image will be clickable', null=True, verbose_name='file link'),
        ),
        migrations.AddField(
            model_name='filersvg',
            name='free_link',
            field=models.CharField(help_text='if present image will be clickable', max_length=2000, null=True, verbose_name='link', blank=True),
        ),
        migrations.AddField(
            model_name='filersvg',
            name='image_url',
            field=models.URLField(default=None, null=True, verbose_name='alternative image url', blank=True),
        ),
        migrations.AddField(
            model_name='filersvg',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Optional. Adds HTML attributes to the rendered link.', blank=True),
        ),
        migrations.AddField(
            model_name='filersvg',
            name='original_link',
            field=models.BooleanField(default=False, help_text='if present image will be clickable', verbose_name='link original image'),
        ),
        migrations.AddField(
            model_name='filersvg',
            name='page_link',
            field=cms.models.fields.PageField(blank=True, to='cms.Page', help_text='if present image will be clickable', null=True, verbose_name='page link'),
        ),
        migrations.AddField(
            model_name='filersvg',
            name='target_blank',
            field=models.BooleanField(default=False, verbose_name='Open link in new window'),
        ),
        migrations.AlterField(
            model_name='filersvg',
            name='image',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.File', null=True, verbose_name='image'),
        ),
    ]
