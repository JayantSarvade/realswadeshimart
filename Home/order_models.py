from django.db import models
from .product_models import Product
from .customer_models import Customer, Customers_Address
from .seller_models import Seller


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('packed', 'packed'),
    ('On the way', 'On the way'),
    ('delivered', 'delivered'),
    ('cancel', 'cancel')
)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customers_address = models.ForeignKey(
        Customers_Address, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    order_total_quantity = models.IntegerField()
    order_datetime = models.DateTimeField()
    order_transaction_id = models.IntegerField()
    order_status_order = models.CharField(
        choices=STATUS_CHOICES, max_length=50)


class Order_Status(models.Model):
    order_status_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_status_remark = models.CharField(max_length=100)
