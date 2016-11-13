# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20161111_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Color'),
        ),
        migrations.AddField(
            model_name='variant',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='product', verbose_name='Product Image', width_field='image_width'),
        ),
        migrations.AddField(
            model_name='variant',
            name='image_height',
            field=models.CharField(default='0', max_length=10, verbose_name='Image Height'),
        ),
        migrations.AddField(
            model_name='variant',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='variant',
            name='image_width',
            field=models.CharField(default='0', max_length=10, verbose_name='Image Width'),
        ),
        migrations.AddField(
            model_name='variant',
            name='link',
            field=models.URLField(blank=True, default='', null=True, verbose_name='Product URL'),
        ),
        migrations.AddField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Product'),
        ),
        migrations.AddField(
            model_name='variant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Size'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='name',
            field=models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Name'),
        ),
    ]