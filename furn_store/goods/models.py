from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return str(self.name)


class Products(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ('id',)

    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}' 
    
    def display_id(self):
        return f'{self.id:05}'
    
    def price_with_discount(self):
        if self.discount:
            return round(self.price * (1 - self.discount/100), 2)
        return self.price


