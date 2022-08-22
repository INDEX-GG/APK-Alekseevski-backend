from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField('first_name', max_length=255, blank=True, null=True)
    last_name = models.CharField('last_name ', max_length=255, blank=True, null=True)
    email = models.EmailField('email ', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
