# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_add_customer_and_alter_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimony',
            options={'verbose_name': 'testimony', 'verbose_name_plural': 'testimonies'},
        ),
        migrations.AddField(
            model_name='developer',
            name='domain',
            field=models.CharField(default='', max_length=50, verbose_name='domain'),
            preserve_default=False,
        ),
    ]