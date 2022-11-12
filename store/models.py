from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib import admin
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.shortcuts import reverse
from uuid import uuid4
# from django_countries.fields import CountryField

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=225)
    discount_price = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=225)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank=True)

    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['title']


class Customer(models.Model):
    MEMBERSHIP_BUYERS = "B"
    MEMBERSHIP_PROFESIONALS = "P"
    MEMBERSHIP_CHOICES = [("B", "Buyers"), ("P", "Profesionals")]
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BUYERS)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order')
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_product_price(self):
        return self.quantity * self.product.unit_price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     ref_code = models.CharField(max_length=20, blank=True, null=True)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     shipping_address = models.ForeignKey(
#         'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
#     billing_address = models.ForeignKey(
#         'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
#     payment = models.ForeignKey(
#         'Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     coupon = models.ForeignKey(
#         'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
#     being_delivered = models.BooleanField(default=False)
#     received = models.BooleanField(default=False)
#     refund_requested = models.BooleanField(default=False)
#     refund_granted = models.BooleanField(default=False)

#     '''
#     1. Item added to cart
#     2. Adding a billing address
#     (Failed checkout)
#     3. Payment
#     (Preprocessing, processing, packaging etc.)
#     4. Being delivered
#     5. Received
#     6. Refunds
#     '''

#     def __str__(self):
#         return self.user.username

#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         if self.coupon:
#             total -= self.coupon.amount
#         return total



class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )
    zip = models.CharField(max_length=6, default=None)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [["cart", "product"]]


# class Address(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     zip = models.CharField(max_length=100)
#     address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
#     default = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         verbose_name_plural = 'Addresses'


# class Payment(models.Model):
#     stripe_charge_id = models.CharField(max_length=50)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.SET_NULL, blank=True, null=True)
#     amount = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


# def userprofile_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         userprofile = UserProfile.objects.create(user=instance)


# post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)