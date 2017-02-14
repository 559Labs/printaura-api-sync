# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_auto_20170212_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bzcreativerendering',
            name='bzcreativelayout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.bzCreativeLayout', verbose_name='Layout'),
        ),
        migrations.AlterField(
            model_name='bzcreativerendering',
            name='pfcatalogfilespec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor_printful.pfCatalogFileSpec', verbose_name='Spec'),
        ),
        migrations.AlterField(
            model_name='bzcreativerendering',
            name='pfprintfile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor_printful.pfPrintFile', verbose_name='Print File'),
        ),
    ]