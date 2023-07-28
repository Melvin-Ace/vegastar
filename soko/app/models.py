from enum import auto
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# create your models here.
STATE_CHOICES = (
    ('Nairobi', 'Nairobi City'),
    ('Mombasa','Mombasa City'),
    ('Kisumu','Kisumu City'),
    ('Nakuru','Nakuru City'),
    ('Wajir','Wajir Town'),
    ('Mandera','Mandera Town'),
    ('Marsabit','Marsabit Town'),
    ('Isiolo','Isiolo Town'),
    ('Meru','Meru Town'),
    ('Tharaka-Nithi','Kathwana Town'),
    ('Embu','Embu Town'),
    ('Kitui','Kitui Town'),
    ('Machakos','Machakos Town'),
    ('Makueni','Wote Town'),
    ('Nyandarua','Ol Kalou Town'),
    ('Nyeri','Nyeri Town'),
    ('Kirinyaga','Kerugoya Town'),
    ('Muranga','Muranga Town'),
    ('Kiambu','Kiambu Town'),
    ('Turkana','Lodway Town'),
    ('West Pokot','Kapenguria Town'),
    ('Samburu','Maralal Town'),
    ('Trans-Nzoia',' Kitale Town'),
    ('Uasin Gishu','Eldoret Town'),
    ('Elgeyo-Marakwet','Iten'),
    ('Nandi','Kapsabet Town'),
    ('Baringo','Kabarnet Town'),
    ('Laikipia','Nanyuki Town'),
    ('Narok','Narok Town'),
    ('Kajiado','Kajiado Town'),
    ('Kericho','Kericho Town'),
    ('Bomet','Bomet Town'),
    ('Kakamega','Kakamega Town'),
    ('Vihiga','Mbale'),
    ('Bungoma','Bungoma Town'),
    ('Busia','Busia Town'),
    ('Siaya','Siaya Town'),
    ('Homa Bay','Homa Bay Town'),
    ('Migori','Migori Town'),
    ('Kisii','Kisii Town'),
    ('kilifi','kilifi Town'),
    ('Nyamira','Nyamira Town'),
    ('Kwale','Kwale Town'),
    ('Tana River','Hola'),
    ('Lamu','Lamu Town'),
    ('Taita-Taveta','Mwatete Town'),
    ('Garissa','Garissa Town'),
)

class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " __ " + self.main_category.name

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    title = models.CharField(max_length=100, default='')
    selling_price = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    short_description = models.TextField(max_length=150, default='')
    product_description = models.TextField(max_length=250, default='')
    keywords = models.CharField(max_length=255, default='')
    product_image = models.ImageField(blank=True, upload_to='product')
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# class Category(MPTTModel):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#     title = models.CharField(max_length=30, unique=True)
#     keywords = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     image = models.ImageField(blank=True, upload_to='images/')
#     status = models.CharField(max_length=10, choices=STATUS)
#     slug = models.SlugField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#     class MPTTMeta:
#         order_insertion_by = ['title']


# class Product(models.Model):
#     sub_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
    # STATUS = (
    #     ('True', 'True'),
    #     ('False', 'False'),
    # )
    # # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # title = models.CharField(max_length=100)
    # selling_price = models.FloatField()
    # discounted_price = models.FloatField()
    # description = models.CharField(max_length=255)
    # composition = models.TextField(default='')
    # prodapp = models.TextField(default='')
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # product_image = models.ImageField(upload_to='product')

    #
    # def __str__(self):
    #     return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    mobile = models.IntegerField(default=0)
    county = models.CharField(choices=STATE_CHOICES, max_length=100, null=True)
    local_town = models.CharField(max_length=50, null=True)



    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES =  (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('on the way', 'On the way'),
    ('delivered', 'delivered'),
    ('cancel', 'Cancel'),
    ('pending', 'Pending'),
)

# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
#     razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
#     razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
#     paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending')
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

