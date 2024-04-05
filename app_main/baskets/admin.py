from django.contrib import admin
from baskets.models import Basket

# admin.site.register(Basket)


class BasketTabAdmin(admin.TabularInline):
    model = Basket
    fields = "product", "quantity", "created_on"
    search_fields = "product", "quantity", "created_on"
    readonly_fields = ("created_on",)
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity", "created_on",]
    list_filter = ["created_on", "user", "product__name",]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Аноним"
    
    def product_display(self, obj):
        return str(object=obj.product.name)