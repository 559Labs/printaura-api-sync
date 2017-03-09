# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20170309_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woostore',
            name='code',
            field=models.CharField(blank=True, default='', help_text='Generally, a two-character uppercase code. Used in SKUs.', max_length=2, null=True, verbose_name='Code'),
        ),
    ]