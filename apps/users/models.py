from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):

    USER_TYPE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STORE_ADMIN', 'Store Admin'),
        ('CLIENT', 'Client')
    )

    user_type = models.CharField(max_length=20,
                                 choices=USER_TYPE_CHOICES,
                                 default='CLIENT')
    
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    