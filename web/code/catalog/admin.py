from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _
from django_extensions.admin import ForeignKeyAutocompleteAdmin


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    fields = [
        'code',
        'name',
        'description',
        'googlecategory',
    ]
    readonly_fields = [
        # 'name',
        'code',
        'googlecategory',
    ]
    suit_classes = 'suit-tab suit-tab-products'


class ItemVariantInline(admin.TabularInline):
    model = ItemVariant
    extra = 5
    fields = [
        'code', 'name',
        # 'image_url',
        # 'link',
        # 'color', 'size',
    ]
    suit_classes = 'suit-tab suit-tab-itemvariants'


class ManufacturerVariantInline(admin.TabularInline):
    model = ManufacturerVariant
    extra = 0
    fields = ['code', 'color', 'size', 'base_price', ]
    readonly_fields = ['code', 'color', 'size', 'base_price', ]
    suit_classes = 'suit-tab suit-tab-ManufacturerVariant'
    ordering = ['size', 'color', ]


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'has_key', ]
    search_fields = ['code', 'name', ]
    form = ManufacturerForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['consumer_url', 'dashboard_url', 'apibase_url']
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['api_key', 'api_hash', ]
        }),
        (_("Notes"), {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width',),
            'fields': ['notes', ]
        }),

    ]
    suit_form_tabs = (
        ('info', _('Info')),
    )
admin.site.register(Manufacturer, ManufacturerAdmin)


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = [
        'tree_actions',
        'indented_title',
        'code',
        'num_items',
    ]
    search_fields = ['code', 'name', ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', 'parent'],
        }),
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('products', _("Items")),
    )
    inlines = (ItemInline, )
admin.site.register(Category, CategoryAdmin)


class GoogleCategoryAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name', ]
admin.site.register(GoogleCategory, GoogleCategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'name',
        'brand',
        'pms_code', 'pms_family',
        'hex_code',
        'r_value', 'g_value', 'b_value',
        'c_value', 'm_value', 'y_value', 'k_value',
    ]
    search_fields = ['code', 'name', ]
    list_filter = [
        ('brand', admin.RelatedOnlyFieldListFilter),
        'pms_family',
    ]
    fieldsets = [
        (None, {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['code', 'name', 'brand', 'color_string'],
        }),
        ("PANTONE", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['pms_code', 'pms_family', ],
        }),
        ("Web Color", {
            'classes': ['suit-tab', 'suit-tab-color', ],
            'fields': [
                'hex_code',
            ],
        }),
        ("RGB Color", {
            'classes': ['suit-tab', 'suit-tab-color', ],
            'fields': [
                'r_value', 'g_value', 'b_value',
            ],
        }),
        ("CMYK Color", {
            'classes': ['suit-tab', 'suit-tab-color', ],
            'fields': [
                'c_value', 'm_value', 'y_value', 'k_value',
            ],
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
        ('color', _('Color')),
    )
admin.site.register(Color, ColorAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'grouping', 'sortorder', ]
    list_filter = ['grouping', ]
    # list_editable = ['code', ]
admin.site.register(Size, SizeAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'has_logo', 'has_description',
        # 'num_vendors',
        'get_num_products',
        'consumer_url', 'wholesale_url'
    ]
    # list_editable = ['code', ]
    inlines = [ItemInline, ]
    form = BrandForm
    search_fields = ['code', 'name', ]
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width',),
            'fields': ['description', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media',),
            'fields': ['image', 'consumer_url', 'wholesale_url', 'product_base_url', ]
        })
    ]
    suit_form_tabs = (
        ('info', _('Info')),
        ('media', _('Media & Web')),
        ('products', _('Items'))
    )
admin.site.register(Brand, BrandAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'code', 'name',
        'brand', 'num_vendors',
        'category', 'googlecategory',
        'age_group', 'gender', 'size_type',
    ]
    # list_editable = ['category', ]
    search_fields = ['name', 'code', ]
    inlines = (ItemVariantInline,)
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('category', admin.RelatedOnlyFieldListFilter),
        ('googlecategory', admin.RelatedOnlyFieldListFilter),
        'age_group',
        'gender',
        'size_type',
    )
    form = ItemForm
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info', ),
            'fields': [
                'code',
                'brand',
                'name',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info', 'full-width', ),
            'fields': [
                'description',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-categorization', ),
            'fields': [
                'category',
                'googlecategory',
            ],
        }),
        ("Metadata", {
            'classes': ('suit-tab', 'suit-tab-categorization', ),
            'fields': [
                'age_group',
                'gender',
                'material',
                'pattern',
            ],
        }),
        ("Sizing", {
            'classes': ('suit-tab', 'suit-tab-categorization', ),
            'fields': [
                'size_type',
                'size_system',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media', ),
            'fields': [
                'link',
                'mobile_link',
            ],
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-media', ),
            'fields': [
                'image',
                'additional_image',
            ],
        }),
    ]
    suit_form_tabs = (
        ('info', _("Info")),
        ('categorization', _("Categorization")),
        ('media', _("Web & Media")),
        ('itemvariants', _("Variants"))

    )
admin.site.register(Item, ItemAdmin)


class ItemVariantAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'product', 'color', 'size', ]
    search_fields = ['name', 'code', 'product__name', ]

    fieldsets = [
        (None, {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['code', 'name', 'product', ],
        }),
        ("Attributes", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['color', 'size', ],
        }),
        ("Media & Web", {
            'classes': ['suit-tab', 'suit-tab-info', ],
            'fields': ['image', 'link', ],
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
    )
admin.site.register(ItemVariant, ItemVariantAdmin)


class ManufacturerItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'item', 'manufacturer',
                    'num_variants', 'num_colors', 'num_sizes',
                    'brand', 'category',
                    )
    search_fields = ('name', 'code',)
    inlines = (ManufacturerVariantInline,)
    list_filter = ['manufacturer', 'brand', 'category', ]
    readonly_fields = ('dt_added', 'dt_updated',)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', 'manufacturer', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['brand', 'item', 'category', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['image_url', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['is_active', 'dt_added', 'dt_updated', ],
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
        ('ManufacturerVariant', _('Manufacturer Variants')),
    )
admin.site.register(ManufacturerItem, ManufacturerItemAdmin)


class ManufacturerVariantAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        # 'name',
        'product',
        'size',
        'color',
    )
    list_filter = ('product', 'size', 'color',)
    search_fields = ('name', 'code',)
    readonly_fields = ('dt_added', 'dt_updated',)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['code', 'name', 'product', 'base_price', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['size', 'color', 'color_code']
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['image_url', ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['is_active', 'dt_added', 'dt_updated', ],
        }),
    ]
    suit_form_tabs = (
        ('info', _('Info')),
    )
admin.site.register(ManufacturerVariant, ManufacturerVariantAdmin)
