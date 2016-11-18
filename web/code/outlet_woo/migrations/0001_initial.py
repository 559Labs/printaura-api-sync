# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creative', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', help_text='READONLY. Unique identifier for the resource.', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', help_text='Product name.', max_length=255, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, default='', help_text='Product slug.', max_length=255, null=True, verbose_name='Slug')),
                ('permalink', models.CharField(blank=True, default='', help_text='READONLY. Product URL.', max_length=255, null=True, verbose_name='Permalink')),
                ('is_active', models.BooleanField(default=False, help_text="Local flag to ensure depreciated products don't break the datastore.", verbose_name='Is Active?')),
                ('app_added', models.DateTimeField(auto_now_add=True, help_text='')),
                ('app_last_sync', models.DateTimeField(auto_now=True, help_text='')),
                ('date_created', models.DateTimeField(blank=True, help_text="READONLY. The date the product was created. In the site's timezone.", null=True, verbose_name='Created')),
                ('date_modified', models.DateTimeField(blank=True, help_text="READONLY. The date the product was last modified, in the site's timezone.", null=True, verbose_name='Modified')),
                ('product_type', models.CharField(choices=[('simple', 'Simple'), ('grouped', 'Grouped'), ('external', 'External'), ('variable', 'Variable')], default='simple', help_text='Product type. Default is simple. In general, do not change this.', max_length=15, verbose_name='Type')),
                ('status', models.CharField(choices=[(('draft',), 'Draft'), ('pending', 'Pending'), ('private', 'Private'), ('publish', 'Publish')], default='publish', help_text='Product status (post status). Default is publish.', max_length=15, verbose_name='Status')),
                ('featured', models.BooleanField(default=False, help_text='Featured product. Default is false.', verbose_name='Featured?')),
                ('catalog_visibility', models.CharField(choices=[('visible', 'Visible'), ('catalog', 'Catalog Only'), ('search', 'Search Only'), ('hidden', 'Hidden')], default='visible', help_text='Catalog visibility. Default is visible. Options: visible (Catalog and search), catalog (Only in catalog), search (Only in search) and hidden (Hidden from all).', max_length=10, verbose_name='Visibility')),
                ('description', models.TextField(blank=True, help_text='Product description.', null=True, verbose_name='Description')),
                ('short_description', models.TextField(blank=True, help_text='Product short description.', null=True, verbose_name='Short Description')),
                ('sku', models.CharField(blank=True, default='', help_text='Unique identifier.', max_length=255, null=True, verbose_name='SKU')),
                ('price', models.CharField(blank=True, default='', help_text='READONLY. Current product price. This is setted from regular_price and sale_price.f', max_length=255, null=True, verbose_name='Price')),
                ('regular_price', models.CharField(blank=True, default='', help_text='Product regular price.', max_length=255, null=True, verbose_name='Regular Price')),
                ('sale_price', models.CharField(blank=True, default='', help_text='Product sale price.', max_length=255, null=True, verbose_name='Sale Price')),
                ('date_on_sale_from', models.DateField(blank=True, help_text='Start date of sale price. Date in the YYYY-MM-DD format.', null=True, verbose_name='On Sale From')),
                ('date_on_sale_to', models.DateField(blank=True, help_text='End date of sale price. Date in the YYYY-MM-DD format.', null=True, verbose_name='On Sale To')),
                ('price_html', models.CharField(blank=True, default='', help_text='READONLY. Price formatted in HTML.', max_length=1000, null=True, verbose_name='Price HTML')),
                ('on_sale', models.BooleanField(default=False, help_text='READONLY. Shows if the product is on sale.', verbose_name='On Sale?')),
                ('purchasable', models.BooleanField(default=True, help_text='READONLY. Shows if the product can be bought.', verbose_name='Purchasable?')),
                ('total_sales', models.IntegerField(default=0, help_text='READONLY. Amount of sales.', verbose_name='Total Sales')),
                ('virtual', models.BooleanField(default=False, help_text='If the product is virtual. Virtual products are intangible and aren’t shipped. Default is false.', verbose_name='Virtual?')),
                ('downloadable', models.BooleanField(default=False, help_text='If the product is downloadable. Downloadable products give access to a file upon purchase. Default is false.', verbose_name='Downloadable?')),
                ('download_limit', models.IntegerField(default=-1, help_text='Amount of times the product can be downloaded, the -1 values means unlimited re-downloads. Default is -1.', verbose_name='Download Limit')),
                ('download_expiry', models.IntegerField(default=-1, help_text='Number of days that the customer has up to be able to download the product, the -1 means that downloads never expires. Default is -1.', verbose_name='Download Expiry')),
                ('download_type', models.CharField(choices=[('standard', 'Standard Product'), ('application', 'Application/Software'), ('music', 'Music')], default='standard', help_text="Download type, this controls the schema on the front-end. Default is standard. Options: 'standard' (Standard Product), application (Application/Software) and music (Music).", max_length=15, verbose_name='Download Type')),
                ('external_url', models.URLField(blank=True, default='', help_text='Product external URL. Only for external products.', null=True, verbose_name='External URL')),
                ('button_text', models.CharField(blank=True, default='', help_text='Product external button text. Only for external products.', max_length=255, null=True, verbose_name='Button Text')),
                ('tax_status', models.CharField(choices=[('taxable', 'Taxable'), ('shipping', 'Shipping Only'), ('none', 'None')], default='taxable', help_text='Tax status. Default is taxable. Options: taxable, shipping (Shipping only) and none.', max_length=15, verbose_name='Tax Status')),
                ('tax_class', models.CharField(blank=True, default='', help_text='The tax class.', max_length=255, null=True, verbose_name='Tax Class')),
                ('manage_stock', models.BooleanField(default=False, help_text='Stock management at product level. Default is false.', verbose_name='Manage Stock')),
                ('stock_quantity', models.IntegerField(default=0, help_text='Stock quantity. If is a variable product this value will be used to control stock for all variations, unless you define stock at variation level.', verbose_name='Stock Quantity')),
                ('in_stock', models.BooleanField(default=True, help_text='Controls whether or not the product is listed as “in stock” or “out of stock” on the frontend. Default is true.', verbose_name='In Stock?')),
                ('backorders', models.CharField(choices=[('no', 'Do Not Allow'), ('notify', 'Allow, But Notify Customer'), ('yes', 'Allow')], default='no', help_text='If managing stock, this controls if backorders are allowed. If enabled, stock quantity can go below 0. Default is no. Options are: no (Do not allow), notify (Allow, but notify customer), and yes (Allow).', max_length=255, verbose_name='Backorders')),
                ('backorders_allowed', models.BooleanField(default=False, help_text='READONLY. Shows if backorders are allowed.', verbose_name='Backorders Allowed?')),
                ('backordered', models.BooleanField(default=False, help_text='READONLY. Shows if a product is on backorder (if the product have the stock_quantity negative).', verbose_name='Backordered?')),
                ('sold_individually', models.BooleanField(default=False, help_text='Allow one item to be bought in a single order. Default is false.', verbose_name='Sold Individually?')),
                ('weight', models.DecimalField(decimal_places=2, default=0, help_text='Product weight in decimal format.', max_digits=10, verbose_name='Weight')),
                ('shipping_required', models.BooleanField(default=False, help_text='READONLY. Shows if the product need to be shipped.', verbose_name='Requires Shipping?')),
                ('shipping_taxable', models.BooleanField(default=False, help_text='READONLY. Shows whether or not the product shipping is taxable.', verbose_name='Taxable Shipping?')),
                ('reviews_allowed', models.BooleanField(default=True, help_text='Allow reviews. Default is true.', verbose_name='Reviewed Allowed?')),
                ('average_rating', models.CharField(blank=True, default='', help_text='READONLY. Reviews average rating.', max_length=15, null=True, verbose_name='Average Rating')),
                ('rating_count', models.IntegerField(default=0, help_text='READONLY. Amount of reviews that the product have.', verbose_name='Rating Count')),
                ('purchase_note', models.CharField(blank=True, default='', help_text='Optional note to send the customer after purchase.', max_length=255, null=True, verbose_name='Purchase Note')),
                ('menu_order', models.IntegerField(default=0, help_text='Menu order, used to custom sort products.', verbose_name='Menu Order')),
                ('design', models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item_design', to='creative.Design')),
                ('parent', models.ForeignKey(blank=True, help_text='Product parent.', null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woo.Product', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Product',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', help_text='Image ID (attachment ID). In write-mode used to attach pre-existing images.', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('app_added', models.DateTimeField(auto_now_add=True, help_text='')),
                ('app_last_sync', models.DateTimeField(auto_now=True, help_text='')),
                ('date_created', models.DateTimeField(blank=True, help_text="READONLY. The date the product was created. In the site's timezone.", null=True, verbose_name='Created')),
                ('date_modified', models.DateTimeField(blank=True, help_text="READONLY. The date the product was last modified, in the site's timezone.", null=True, verbose_name='Modified')),
                ('src', models.URLField(help_text='In write-mode used to upload new images.', verbose_name='Image URL')),
                ('alt', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Alternative Text')),
                ('position', models.IntegerField(default=1, help_text='0 means that the image is featured.', verbose_name='Image Position')),
                ('image_height', models.CharField(default='0', max_length=10, verbose_name='Image Height')),
                ('image_width', models.CharField(default='0', max_length=10, verbose_name='Image Width')),
                ('image', models.ImageField(blank=True, height_field='image_height', null=True, upload_to='outlet_woo/productimage', verbose_name='Local Image', width_field='image_width')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woo.Product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('web_url', models.URLField(blank=True, default='', null=True, verbose_name='Website')),
                ('consumer_key', models.CharField(blank=True, max_length=43, null=True, verbose_name='Consumer Key')),
                ('consumer_secret', models.CharField(blank=True, max_length=43, null=True, verbose_name='Consumer Secret')),
                ('timezone', timezone_field.fields.TimeZoneField(default='America/New_York')),
                ('num_products', models.IntegerField(default=0, verbose_name='Product Count')),
                ('last_sync', models.DateTimeField(auto_now=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Shop',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'Shop',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woo.Shop'),
        ),
    ]
