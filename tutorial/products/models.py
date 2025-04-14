from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=256, blank=False)
    content = models.TextField(max_length=128, blank=False)
    price = models.DecimalField(default=99.99,max_digits=15, decimal_places=2)


    @property
    def sale_price(self):
        return f"{float(self.price) * 0.8:.2f}"
    
    def get_discount(self):
        return "122"


    