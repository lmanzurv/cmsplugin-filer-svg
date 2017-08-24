# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerSVG',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', filer.fields.file.FilerFileField(to='filer.File')),
            ],
            options={
                'verbose_name': 'SVG Image',
                'verbose_name_plural': 'SVG Images',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
