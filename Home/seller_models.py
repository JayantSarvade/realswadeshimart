from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


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


class Seller(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    shop_name = models.CharField(max_length=60)
    shop_address_line1 = models.CharField(max_length=60)
    shop_address_line2 = models.CharField(max_length=60)
    shop_state = models.CharField(choices=STATE_CHOICES, max_length=45)
    shop_city = models.CharField(max_length=45)
    shop_pincode = models.IntegerField()
    shop_mobile_number = models.IntegerField()
    shop_mail_id = models.EmailField(unique=True)
    shop_gstin_number = models.CharField(max_length=45)
    pan_card_number = models.CharField(max_length=45, unique=True)


class Seller_Bank_Details(models.Model):
    seller_bank_details_id = models.IntegerField(primary_key=True)
    seller_id = models.ForeignKey(Seller, on_delete=CASCADE)
    bank_name = models.CharField(max_length=60)
    bank_branch_name = models.CharField(max_length=60)
    account_number = models.IntegerField(unique=True)
    ifsc_code = models.CharField(max_length=45)
