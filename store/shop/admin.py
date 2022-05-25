from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.safestring import mark_safe
from .models import Product, ProductCategory, ProductImages, RatingStar, Reviews, Cart


# admin.site.register(ProductCategory, MPTTModelAdmin)
admin.site.register(
    ProductCategory,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Products"""
    list_display = ('name', 'price', 'category', 'quantity', 'get_image', 'published')
    actions = ["publish", "unpublished"]

    def get_image(self, obj=None):
        if obj:
            return mark_safe(f"<img src={obj.image.url} width='35' height='45'")
        else:
            pass

    def unpublished(self, request, queryset):
        """Remove product from sale action"""
        row_update = queryset.update(published=False)
        if row_update == '1':
            message_bit = '1 product updated'
        else:
            message_bit = f"{row_update} products updated"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Publish product action"""
        row_update = queryset.update(published=True)
        if row_update == '1':
            message_bit = '1 product updated'
        else:
            message_bit = f"{row_update} products updated"
        self.message_user(request, f"{message_bit}")

    publish.short_description = 'Publish'
    publish.allowed_permissions = ('change', )

    unpublished.short_description = 'Unpublished'
    unpublished.allowed_permissions = ('change', )


admin.site.register(RatingStar)
admin.site.register(ProductImages)
admin.site.register(Reviews)
admin.site.register(Cart)
