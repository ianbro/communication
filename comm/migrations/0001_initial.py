# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('deactivated', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('deactivated', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Worker')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
                ('users_read', models.ManyToManyField(blank=True, related_name='viewers_request', to='core.Worker')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comm.Request'),
        ),
        migrations.AddField(
            model_name='comment',
            name='users_read',
            field=models.ManyToManyField(blank=True, related_name='viewers_comment', to='core.Worker'),
        ),
    ]