# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_boarditem_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarditem',
            name='written_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
