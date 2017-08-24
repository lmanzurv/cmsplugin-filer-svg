# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_svg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filersvg',
            name='image',
            field=models.FileField(upload_to=b'svg/20160705/'),
        ),
    ]
