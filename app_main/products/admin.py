from django.contrib import admin
from products.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "price", "discount", "sell_price", "category"]
    list_editable = ["price", "discount", "category"]
    search_fields = ["name", "description"]
    list_filter = ["price", "discount", "category"]
    fields = [
        "name",
        "category",
        "description",
        "image",
        ("price", "discount"),
        "slug"
    ]