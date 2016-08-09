# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boarditem',
            name='private',
            field=models.BooleanField(default=False, verbose_name='비밀글 여부'),
        ),
    ]
