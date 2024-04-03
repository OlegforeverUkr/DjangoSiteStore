from django.db import models

from products.models import Products
from users.models import User


class BasketQuerySet(models.QuerySet):
    
    def total_price_all_users_baskets(self):
        return sum([cart.products_price() for cart in self])

    def total_quantity(self):
        if self:
            return sum([cart.quantity for cart in self])
        return 0


class Basket(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Дата/Время добавления")

    class Meta:
        db_table = "baskets"
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"
        ordering = ['created_on']

    objects = BasketQuerySet().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Корзина {self.user.username} / Товар {self.product.name}"