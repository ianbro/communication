# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 12:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0022_auto_20160329_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('code', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('groups_required', models.ManyToManyField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_manager', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('developer', models.BooleanField(default=False)),
                ('picture_field', models.ImageField(blank=True, null=True, upload_to=b'/Users/kirkp1ia/projects/communication/profile_pics/profile_pics')),
                ('desks', models.ManyToManyField(to='core.Desk')),
                ('globalid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projects', models.ManyToManyField(to='core.Project')),
            ],
        ),
    ]
