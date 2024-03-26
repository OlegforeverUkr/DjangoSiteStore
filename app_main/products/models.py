from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, verbose_name="URL")
    display_number = models.IntegerField(default=0)

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ['display_number', 'name']

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="product_images", blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0.0, max_digits=5, decimal_places=1, verbose_name="Цена")
    discount = models.DecimalField(default=0, max_digits=3, decimal_places=1, verbose_name="Скидка (%)")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    category = models.ForeignKey(to=Categories, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория товара")

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['id']


    def __str__(self):
        return self.name
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price*self.discount)/100, 2)

        return self.price