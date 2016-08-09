# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='제목', max_length=100)),
                ('content', models.TextField(verbose_name='내용')),
                ('written_from', models.CharField(verbose_name='REMOTE_ADDR', max_length=100)),
                ('created_at', models.DateTimeField(verbose_name='생성일', default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(verbose_name='수정일', default=django.utils.timezone.now)),
                ('locked', models.BooleanField(verbose_name='글 수정 불가 여부', default=False)),
                ('written_by', models.OneToOneField(verbose_name='작성자', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글',
            },
        ),
    ]
