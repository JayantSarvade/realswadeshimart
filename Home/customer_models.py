from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    user_id = models.OneToOneField(User, null=True, on_delete=CASCADE)
    customer_mobile_number = models.IntegerField(null=True)
    customer_alternate_number = models.IntegerField(null=True)
    customer_profile_picture = models.FileField(null=True, blank=True)
    wishlist_product_id = models.CharField(null=True, max_length=45)
    cart_product_id = models.CharField(null=True, max_length=45)
    customer_otp = models.CharField(max_length=6, blank=True)


class Payment_Methods(models.Model):
    payment_methods_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    payment_methods = models.CharField(max_length=45)
    card_number = models.IntegerField()
    card_holder_name = models.CharField(max_length=45)
    card_expiry_date = models.DateField()
    mobile_number = models.IntegerField()


STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu',
     'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry')

)


ADDRESS_CHOICES = (
    ('Home', 'Home'),
    ('Office', 'Office'),
)


class Customers_Address(models.Model):
    customers_address_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    address_line1 = models.CharField(max_length=60)
    address_line2 = models.CharField(max_length=60)
    state = models.CharField(choices=STATE_CHOICES, max_length=45)
    city = models.CharField(max_length=45)
    pincode = models.IntegerField()
    address_type = models.CharField(choices=ADDRESS_CHOICES, max_length=45)
    feasible_delivery_time = models.DurationField()
