# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 21:36
from __future__ import unicode_literals

import colorfield.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='images/developer/', verbose_name='avatar')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('github', models.URLField(blank=True, verbose_name='github')),
                ('twitter', models.URLField(blank=True, verbose_name='twitter')),
                ('linkedin', models.URLField(blank=True, verbose_name='linkedIn')),
                ('stackoverflow', models.URLField(blank=True, verbose_name='stackOverFlow')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'
                )),
            ],
            options={
                'verbose_name': 'developer',
                'verbose_name_plural': 'developer',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('developer', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='portfolio.Developer', verbose_name='developer'
                )),
            ],
            options={
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
                'ordering': ['date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, verbose_name='name')),
                ('image', models.ImageField(upload_to='images/developer/', verbose_name='avatar')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('entry', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='portfolio.Entry', verbose_name='entry'
                )),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='portfolio.Tag', verbose_name='tags'),
        ),
    ]
