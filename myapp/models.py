from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cart.pk} - {self.product.name}'

    def total_price(self):
        return self.quantity * self.product.price


class Cart(models.Model):
    products = models.ManyToManyField('Product', through='CartItem')

    def __str__(self):
        return f'Cart of {self.pk} ({self.products.count()})'

    def total_price(self):
        return sum(item.total_price() for item in self.cartitem_set.all())
