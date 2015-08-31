# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='name',
            field=models.CharField(default=123, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='fullname',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
