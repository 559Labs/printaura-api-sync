# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pfCatalogColor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Color')),
                ('code', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Color Code')),
            ],
            options={
                'verbose_name_plural': 'Catalog Colors',
                'verbose_name': 'Catalog Color',
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='pfCatalogFileSpec',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Name')),
                ('note', models.TextField(blank=True, default='', null=True, verbose_name='Note')),
                ('width', models.IntegerField(default=0, verbose_name='Width')),
                ('height', models.IntegerField(default=0, verbose_name='Height')),
            ],
            options={
                'verbose_name_plural': 'File Specs',
                'verbose_name': 'File Spec',
                'ordering': ['name', 'width', 'height'],
            },
        ),
        migrations.CreateModel(
            name='pfCatalogFileType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('pid', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Printful ID')),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Title')),
                ('additional_price', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Additional Price')),
                ('pfcatalogfilespec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogFileSpec', verbose_name='File Spec')),
            ],
            options={
                'verbose_name_plural': 'Catalog File Types',
                'verbose_name': 'Catalog File Type',
                'ordering': ['title', 'pid'],
            },
        ),
        migrations.CreateModel(
            name='pfCatalogOptionType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('pid', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Printful ID')),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Title')),
                ('type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Type')),
                ('additional_price', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Additional Price')),
            ],
            options={
                'verbose_name_plural': 'Catalog Option Types',
                'verbose_name': 'Catalog Option Type',
                'ordering': ['title', 'pid'],
            },
        ),
        migrations.CreateModel(
            name='pfCatalogProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, help_text='', verbose_name='Is Active?')),
                ('pid', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Printful ID')),
                ('type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Type')),
                ('brand', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Brand')),
                ('model', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Model')),
                ('image', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Image')),
                ('variant_count', models.IntegerField(default=0, verbose_name='Variant Count')),
            ],
            options={
                'verbose_name_plural': 'Catalog Products',
                'verbose_name': 'Catalog Product',
                'ordering': ['brand', 'model', 'pid'],
            },
        ),
        migrations.CreateModel(
            name='pfCatalogSize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Size')),
            ],
            options={
                'verbose_name_plural': 'Catalog Size',
                'verbose_name': 'Catalog Size',
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='pfCatalogVariant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('pid', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Printful ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('image', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Image')),
                ('price', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Price')),
                ('in_stock', models.BooleanField(default=False, verbose_name='In Stock')),
                ('pfcatalogproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogProduct', verbose_name='Product')),
                ('pfcolor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogColor', verbose_name='Color')),
                ('pfsize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogSize', verbose_name='Size')),
            ],
            options={
                'verbose_name_plural': 'Catalog Variants',
                'verbose_name': 'Catalog Variant',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='pfCountry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
                'ordering': ['name', 'code'],
            },
        ),
        migrations.CreateModel(
            name='pfPrintFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('pid', models.IntegerField(default=0, verbose_name='Printful ID')),
                ('type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Type')),
                ('hash', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Hash')),
                ('url', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='URL')),
                ('filename', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Filename')),
                ('mime_type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='MIME Type')),
                ('size', models.IntegerField(default=0, verbose_name='Size')),
                ('width', models.IntegerField(default=0, verbose_name='Width')),
                ('height', models.IntegerField(default=0, verbose_name='Height')),
                ('dpi', models.IntegerField(default=0, verbose_name='DPI')),
                ('status', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Status')),
                ('created', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Created')),
                ('thumbnail_url', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Thumbnail URL')),
                ('preview_url', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Preview URL')),
                ('visible', models.BooleanField(default=False, verbose_name='Visible')),
            ],
            options={
                'verbose_name_plural': 'Print Files',
                'verbose_name': 'Print File',
                'ordering': ['pid', 'type'],
            },
        ),
        migrations.CreateModel(
            name='pfState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('pfcountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCountry', verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'States',
                'verbose_name': 'State',
                'ordering': ['name', 'code'],
            },
        ),
        migrations.CreateModel(
            name='pfStore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('website', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Website')),
                ('created', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Created')),
                ('consumer_key', models.CharField(blank=True, default='', max_length=64, verbose_name='API Consumer Key')),
                ('consumer_secret', models.CharField(blank=True, default='', max_length=64, verbose_name='API Consumer Secret')),
            ],
            options={
                'verbose_name_plural': 'Stores',
                'verbose_name': 'Store',
                'ordering': ['name', 'code'],
            },
        ),
        migrations.CreateModel(
            name='pfSyncItemOption',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('pid', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Printful ID')),
                ('value', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name_plural': 'Sync Item Options',
                'verbose_name': 'Sync Item Option',
                'ordering': ['pid'],
            },
        ),
        migrations.CreateModel(
            name='pfSyncProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('pid', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Printful ID')),
                ('external_id', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='External ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('variants', models.IntegerField(default=0, verbose_name='Variant Count')),
                ('synced', models.IntegerField(default=0, verbose_name='Synced')),
                ('pfstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfStore', verbose_name='Store')),
            ],
            options={
                'verbose_name_plural': 'Sync Products',
                'verbose_name': 'Sync Product',
                'ordering': ['name', 'pid'],
            },
        ),
        migrations.CreateModel(
            name='pfSyncVariant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('pid', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Printful ID')),
                ('external_id', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='External ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('synced', models.BooleanField(default=False, verbose_name='Synced')),
                ('files', models.ManyToManyField(blank=True, to='vendor_printful.pfPrintFile')),
                ('pfcatalogvariant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogVariant', verbose_name='Catalog Variant')),
                ('pfsyncproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfSyncProduct', verbose_name='Sync Product')),
            ],
            options={
                'verbose_name_plural': 'Sync Variants',
                'verbose_name': 'Sync Variant',
                'ordering': ['name', 'pid'],
            },
        ),
        migrations.AddField(
            model_name='pfsyncitemoption',
            name='pfsyncvariant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfSyncVariant'),
        ),
        migrations.AddField(
            model_name='pfprintfile',
            name='pfstore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfStore'),
        ),
        migrations.AddField(
            model_name='pfcatalogoptiontype',
            name='pfcatalogvariant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogVariant'),
        ),
        migrations.AddField(
            model_name='pfcatalogfiletype',
            name='pfcatalogvariant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogVariant', verbose_name='Variant'),
        ),
    ]