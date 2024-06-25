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
import uuid

class Order(models.Model):
    order_no = models.CharField(max_length=100, unique=True, editable=False, primary_key=True)
    product_name = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, related_name='orders_created', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.product_name


    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = self.generate_order_no()
        super(Order, self).save(*args, **kwargs)

    def generate_order_no(self):
        return str(uuid.uuid4()).replace('-', '').upper()[:3]  # Generates a unique order number
