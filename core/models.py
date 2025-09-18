from django.db import models

class Product(models.Model):
    url = models.URLField(max_length=1024, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    desired_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or self.url

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - R$ {self.price}"