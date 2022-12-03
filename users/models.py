from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True)

# class User(AbstractUser):
#     MEMBERSHIP_BUYERS = "B"
#     MEMBERSHIP_PROFESIONALS = "P"
#     MEMBERSHIP_FREELANCERS = "F"
#     MEMBERSHIP_CHOICES = [("B", "Buyers"), ("P", "Profesionals"), ("F", "Freelancers")]
#     phone = models.CharField(max_length=255)
#     birth_date = models.DateField(null=True, blank=True)
#     membership = models.CharField(
#         max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BUYERS)
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'

#     @admin.display(ordering='user__first_name')
#     def first_name(self):
#         return self.user.first_name

#     @admin.display(ordering='user__last_name')
#     def last_name(self):
#         return self.user.last_name

#     class Meta:
#         ordering = ['user__first_name', 'user__last_name']
#         permissions = [
#             ('view_history', 'Can view history')
#         ]
