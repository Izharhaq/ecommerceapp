# from django.db import models

# Create your models here.

# from django.contrib.auth.models import User
# from products.models import Product

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     ordered_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"
    


from django.db import models
from accounts.models import CustomUser

class Order(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

